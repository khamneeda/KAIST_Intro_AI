import gym
import numpy as np
import time, pickle, os
import parameters as params
from q_updater import Qlearning_updater as Q_up
import modi
import time



class trainer():
    def __init__(self, params):
        self.size_idx = params["size_idx"]
        self.map_name = params["map_name"]
        self.epsilon = params["epsilon"]
        self.epochs = params["epochs"]
        self.max_steps = params["max_steps"]
        self.lr = params["lr"]
        self.gamma = params["gamma"]

        self.Train_render = params["Train_render"]
        self.Test_Visrender = params["Test_Visrender"]
        self.save_result = params["save_result"]

        self.env = gym.make(params["env"], is_slippery = params["is_slippery"], 
            map_name = self.map_name)

    def train(self): 
        size = self.size_idx[self.map_name]

        l_idx = ['left', 'down', 'right', 'up']
        print("TRAINING...")
        updater = Q_up(self.env, self.epsilon, self.gamma, self.lr)

        for episode in range(self.epochs):
            state = self.env.reset()
            t = 0
            reward_sum = 0
            while t < self.max_steps:
                if self.Train_render:
                    self.env.render()
                action = updater.action_strategy(state)
                state2, reward, done, info = self.env.step(action)  
                Q = updater.Bellman_Q_updater(state, state2, reward, action)
                state = state2
                t += 1
                reward_sum += reward
                if done:
                    break
            
            # if episode != 0 and episode % 1000 == 0:
            # if episode != 0:

            #     print("EPISODE: %d, CURRENT_REWARD: %d" % (episode + 1, reward_sum))

        print("TRAINING DONE.")
        res_path = np.argmax(Q, axis = 1)
        res_wpath = np.array([l_idx[x] for x in res_path]).reshape(-size, size)
        
        print("Q-tables: ")
        print(Q)
        # Our code
        print("Run path:", res_wpath)

        bundle = modi.MODI()
        network = bundle.networks[0]
        button = bundle.networks[0]
        motor = bundle.motors[0]
        gyro = bundle.gyros[0]

        self.car_run(res_wpath, network,motor,gyro)

        if self.Test_Visrender:
            dataDic = self.env.our_render()
            import griddrawer as gd

            rend = gd.OUR_RENDERER(dataDic, size)
            rend.renderer(res_wpath)

        if self.save_result:
            with open("FrozenLake" + self.map_name + "_" + str(self.epochs) + "iters.pkl", 'wb') as f:
                pickle.dump(Q, f)

    def move(self, dir, prev, network,motor,gyro):
        change = prev - dir
        
        #turn left : + +, 1115ms
        if (change == 1 or change == -3):
            motor.speed = 40,40
            time.sleep(1.115)
        
        #turn right : -40 -40, 1115ms
        elif (change == -1 or change == 3):
            motor.speed = -40,-40
            time.sleep(1.115)
        
        #move forward : 69  -70, 1525
        elif (change == 0):
            motor.speed = 69,-70
            time.sleep(1.525)

        #turn back
        elif (change == 2 or change == -2):
            pass

        else:
            print("Turn error occured")
            pass # move forward
         

    def car_run(self, path, network,motor,gyro):
        # path making
        pos = [0,0] # rows, column : m, n in matrix
        prev_int = 2 # left : 0, up: 1, right: 2, down: 3
        dir_int = 0
        while (pos != [7,7]):
            direction = path[pos[0], pos[1]]
            match direction:
                case "down":
                    pos[0] += 1
                    dir_int = 3
                case "up":
                    pos[0] -= 1
                    dir_int = 1
                case "left":
                    pos[1] -= 1
                case "right":
                    pos[1] += 1
                    dir_int = 2
            print("Direction", direction, "Pos:", pos, "Prev:", prev_int, "/ Dir:", dir_int)

            self.move(dir_int, prev_int, network,motor,gyro)
            prev_int = dir_int
        motor.speed = 0,0
        print("Arrived")
                    
                    
if __name__ == "__main__":
    params = params.PARAMS
    if params["Test_Visrender"]:
        try:
            from pip import main as pipmain
        except:
            from pip._internal import main as pipmain
        def install(package):
            pipmain(['install', package])
        install("pygame")
    trainer = trainer(params)
    trainer.train()