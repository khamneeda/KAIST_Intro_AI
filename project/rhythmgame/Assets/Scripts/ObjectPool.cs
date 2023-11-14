using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectPool : MonoBehaviour
{
    public static ObjectPool Instance;

    [SerializeField]
    private GameObject poolingObjectPrefab;

    private Queue<Note> poolingObjectQueue = new Queue<Note>();

    private void Awake()
    {
        Instance = this;
        Initialize(200);
    }

    // ������Ʈ Ǯ �ȿ� ������Ʈ�� �������� ���� �� �Ǵ� ������Ʈ Ǯ �ʱ�ȭ �ÿ� �̸� ����� ���� ������Ʈ�� �����ϴ� �Լ�
    private Note CreateNewObject()
    {
        // ������Ʈ Ǯ�� �ڽ� ������Ʈ�� ��Ʈ�� �̸� ����� ��Ȱ��ȭ
        Note note = Instantiate(poolingObjectPrefab, transform).GetComponent<Note>();
        note.gameObject.SetActive(false);
        return note;
    }

    private void Initialize(int count)
    {
        for(int i = 0; i < count; i++)
        {
            poolingObjectQueue.Enqueue(CreateNewObject());
        }
    }

    // ������Ʈ Ǯ���� ������Ʈ�� ������ ����, ���� ������ ������Ʈ�� ���ٸ� ���� ����
    public static Note GetObject()
    {
        GameObject notesOnActive = GameObject.Find("NotesOnActive");

        if(Instance.poolingObjectQueue.Count > 0)
        {
            Note note = Instance.poolingObjectQueue.Dequeue();
            note.transform.SetParent(notesOnActive.transform);
            note.gameObject.SetActive(true);
            return note;
        }
        else
        {
            Note note = Instance.CreateNewObject();
            note.transform.SetParent(notesOnActive.transform);
            note.gameObject.SetActive(true);
            return note;
        }
    }

    // ����� ���� ������Ʈ�� ������Ʈ Ǯ�� �ݳ�
    public static void ReturnObject(Note note)
    {
        note.gameObject.SetActive(false);
        note.transform.SetParent(Instance.transform);
        Instance.poolingObjectQueue.Enqueue(note);
    }
}