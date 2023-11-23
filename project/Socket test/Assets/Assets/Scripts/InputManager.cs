using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InputManager : MonoBehaviour
{
    Judgement judgement;
    public int a1,a2,a3,a4,a5;
    bool b1, b2, b3, b4, b5,b11,b22,b33,b44,b55;

    void Start()
    {
        judgement = FindObjectOfType<Judgement>().GetComponent<Judgement>();
    }

    void Update()
    {

        a1 = GameObject.Find("Socket").GetComponent<UdpSocket>().lf;
        a2 = GameObject.Find("Socket").GetComponent<UdpSocket>().lb;
        a3 = GameObject.Find("Socket").GetComponent<UdpSocket>().mid;
        a4 = GameObject.Find("Socket").GetComponent<UdpSocket>().rf;
        a5 = GameObject.Find("Socket").GetComponent<UdpSocket>().rb;
        /*
        if (Input.GetKeyDown(KeyCode.Z))
        {
            judgement.GetDiffTime(1);
        }

        if (Input.GetKeyDown(KeyCode.X))
        {
            judgement.GetDiffTime(2);
        }

        if (Input.GetKeyDown(KeyCode.Period))
        {
            judgement.GetDiffTime(3);
        }

        if (Input.GetKeyDown(KeyCode.Slash))
        {
            judgement.GetDiffTime(4);
        }

        if (Input.GetKeyDown(KeyCode.Comma))
        {
            judgement.GetDiffTime(5);
        }
        */
        if (a1 == 1)
        {
            b1 = true;
        }
        else b1 = false;
        if (a2 == 1)
        {
            b2 = true;
        }
        else b2 = false;
        if (a3 == 1)
        {
            b3 = true;
        }
        else b3 = false;
        if (a4 == 1)
        {
            b4 = true;
        }
        else b4 = false;
        if (a5 == 1)
        {
            b5 = true;
        }
        else b5 = false;


        if (b11!=b1 && b1)
        {
            judgement.GetDiffTime(1);
        }
        if (b22 != b2 && b2)
        {
            judgement.GetDiffTime(2);
        }
        if (b33 != b3 && b3)
        {
            judgement.GetDiffTime(3);
        }
        if (b44 != b4 && b4)
        {
            judgement.GetDiffTime(4);
        }
        if (b55 != b5 && b5)
        {
            judgement.GetDiffTime(5);
        }

        b11 = b1;
        b22 = b2;
        b33 = b3;
        b44 = b4;
        b55 = b5;

    }
}