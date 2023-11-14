using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Conductor : MonoBehaviour
{
    public AudioSource songPlayer;
    public AudioSource hitSoundPlayer;
    public AudioClip hitSound;

    Chart chart;
    Parser parser;
    Judgement judgement;
    BGAPlayer bgaPlayer;

    public float startYPos;
    public float endYPos;

    // �뷡�� BPM
    public float songBpm;

    // ���� �뷡�� ��� ��ġ
    public float songPosition;

    // �� ���ڿ� �ҿ�Ǵ� �ð����� (60f / BPM)�� ����
    // public float secondsPerBeat;

    // �Է� ������
    public float globalOffset;

    // �뷡 ����� ���۵� ������ �����Ͽ� songPosition�� ����� �� ���־�� ��
    public float dspTimeSong;

    // ��Ʈ ���� �������� ��Ʈ �ı� �������� ǥ�õ� �� �ִ� �ִ� ���� �� (��ũ�� �ӵ�)
    public float beatsShownOnScreen;

    bool isSongStarted = false;
    bool isBGAStarted = false;

    float videoStartTime;
    public float bgaOffset;

    void Start()
    {
        chart = FindObjectOfType<Chart>().GetComponent<Chart>();
        parser = FindObjectOfType<Parser>().GetComponent<Parser>();
        judgement = FindObjectOfType<Judgement>().GetComponent<Judgement>();
        bgaPlayer = FindObjectOfType<BGAPlayer>().GetComponent<BGAPlayer>();
        beatsShownOnScreen = 1.6f;
        //globalOffset = -0.15f;
        globalOffset = 0f;
        bgaOffset = 1.6f;
        hitSound = hitSoundPlayer.clip;
    }

    void Update()
    {
        // ��Ʈ ������ �Ľ��� �� �ɶ����� ���
        if (parser.isParsed)
        {
            songBpm = (float)chart.timingList[0].bpm * songPlayer.pitch;
            //songBpm = Mathf.Round((1f / (float)chart.timingList[0].bpm  * 1000f * 60f) * 100f) / 100f * songPlayer.pitch;
            //secondsPerBeat = 60f / songBpm;
        }
        else
        {
            return;
        }

        // �����̽��ٸ� ������ ����
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (!isSongStarted)
            {
                isSongStarted = true;
                // 3�� �ڿ� ����
                dspTimeSong = (float)AudioSettings.dspTime + 3f;
                songPlayer.PlayDelayed(3f);
                videoStartTime = Time.time;
                return;
            }
        }

        if (!isSongStarted) return;

        if (!isBGAStarted)
        {
            if (Time.time - videoStartTime >= 3f + bgaOffset)
            {
                isBGAStarted = true;
                bgaPlayer.PlayVideo();
            }
        }

        // Ư�� �뷡���� ���� �κп� �ణ�� ������ �ֱ� ������ �뷡 ��ġ�� ����� �� �� ���鸸ŭ ���־�� ��
        songPosition = (float)(AudioSettings.dspTime - dspTimeSong + chart.offset + globalOffset) * songPlayer.pitch;

        float noteToSpawn = songPosition * 1000 / songBpm + beatsShownOnScreen;

        if (chart.track1_TimingData.Count > 0)
        {
            float nextTimeInTrack1 = chart.track1_TimingData.Peek() / songBpm;

            if (nextTimeInTrack1 < noteToSpawn)
            {
                Note note = ObjectPool.GetObject();
                note.Initialize(this, -2.25f, startYPos, endYPos, chart.track1_TimingData.Dequeue(), nextTimeInTrack1);
                judgement.EnqueueNote(1, note);
            }
        }

        if (chart.track2_TimingData.Count > 0)
        {
            float nextTimeInTrack2 = chart.track2_TimingData.Peek() / songBpm;

            if (nextTimeInTrack2 < noteToSpawn)
            {
                Note note = ObjectPool.GetObject();
                note.Initialize(this, -0.75f, startYPos, endYPos, chart.track2_TimingData.Dequeue(), nextTimeInTrack2);
                judgement.EnqueueNote(2, note);
            }
        }

        if (chart.track3_TimingData.Count > 0)
        {
            float nextTimeInTrack3 = chart.track3_TimingData.Peek() / songBpm;

            if (nextTimeInTrack3 < noteToSpawn)
            {
                Note note = ObjectPool.GetObject();
                note.Initialize(this, 0.75f, startYPos, endYPos, chart.track3_TimingData.Dequeue(), nextTimeInTrack3);
                judgement.EnqueueNote(3, note);
            }
        }

        if (chart.track4_TimingData.Count > 0)
        {
            float nextTimeInTrack4 = chart.track4_TimingData.Peek() / songBpm;

            if (nextTimeInTrack4 < noteToSpawn)
            {
                Note note = ObjectPool.GetObject();
                note.Initialize(this, 2.25f, startYPos, endYPos, chart.track4_TimingData.Dequeue(), nextTimeInTrack4);
                judgement.EnqueueNote(4, note);
            }
        }
    }
}