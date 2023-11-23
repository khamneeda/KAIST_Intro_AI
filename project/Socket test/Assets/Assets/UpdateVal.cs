using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Updateval : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        UdpSocket clientSocket = GetComponent<UdpSocket>();  
        Debug.Log(clientSocket.lf);
        Debug.Log(clientSocket.rf);
        Debug.Log(clientSocket.mid);
        Debug.Log(clientSocket.lb);
        Debug.Log(clientSocket.rb);


    }
}
