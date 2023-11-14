using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Note : MonoBehaviour
{
    Conductor conductor;

    // ��Ʈ ���� ��ġ
    public float spawnPos;

    // ������ ��ġ
    public float judgementLinePos;

    public int columnNum;

    // ������ �Ʒ��� ������ ��Ʈ�� �ı� ��ġ
    // public float destroyPos = -6f;

    // ��Ʈ�� �ð���
    public float timing;

    // ��Ʈ�� �ð����� ���� ������ ��ȯ�� ��
    public float beat;

    public void Initialize(Conductor conductor, float xPos, float startYPos, float endYPos, float timing, float beat)
    {
        this.conductor = conductor;
        this.spawnPos = startYPos;
        this.judgementLinePos = endYPos;
        this.timing = timing;
        this.beat = beat;

        transform.position = new Vector2(xPos, spawnPos);
    }

    void Start()
    {

    }

    void Update()
    {
        // (judgementLinePos - spawnPos)�� ��Ʈ ���� �������� �ı� ���������� �����̸�, �� ���� Ŀ������ ��Ʈ�� �� �Ʒ��� ������

        // (beat - conductor.songPosition / conductor.secondsPerBeat) / conductor.beatsShownOnScreen�� 
        // �������� ��Ʈ�� ���� ���� ���� �뷡 ��ġ�� ���� ���� ���� ȭ�鿡 ǥ���� �ִ� ���� ��(��ũ�� �ӵ�)�� ���� ����
        // ���� ���, beatsShownOnScreen�� ���� 4���, (beat - conductor.songPosition / conductor.secondsPerBeat)�� ���� 0~4�� ��Ʈ�� ȭ�鿡 ����

        // 1���� ���� ���� �� ���� (1f - (beat - conductor.songPosition / conductor.secondsPerBeat) / conductor.beatsShownOnScreen)��
        // (judgementLinePos - spawnPos)�� ���ؾ� ��Ʈ�� �������� �� ó�� ���̰� ��

        // ����ϸ�, �������� ��Ʈ�� ���� ���� ���� �뷡 ��ġ�� ���� ���� ���� beatsShownOnScreen�� ������ ��Ʈ�� �����ǰ�
        // (��Ʈ�� ���� �� - ���� �뷡 ��ġ�� ���� ��)�� 0�� ����� ������ ��Ʈ�� �������� ��������� ��

        transform.position = new Vector2(transform.position.x,
            spawnPos + (judgementLinePos - spawnPos) * 
            (1f - (beat - conductor.songPosition * 1000 / conductor.songBpm) / conductor.beatsShownOnScreen));

        /*if (transform.position.y <= destroyPos)
        {
            ObjectPool.ReturnObject(this);
        }*/
    }
}