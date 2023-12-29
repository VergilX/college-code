import java.io.*;

class Queue
{
    private int max;
    private int[] arr;
    public int rear, front;

    public Queue(int s)
    {
        max = s;
        rear = -1;
        front = 0;
        arr = new int[max];
    }

    public void insert(int j)
    {
        if (rear == max-1)
        {
            rear = -1;
        }
        arr[++rear] = j;
    }

    public int delete()
    {
        int temp = arr[front++];
        if (front == max)
        {
            front = 0;
        }
        return temp;
    }

    public int peek()
    {
        return arr[front];
    }

    public boolean isEmpty()
    {
        return (((rear+1) % max) == front);
    }

    public boolean isFull()
    {
        return (((rear+2) % max) == front);
    }

    public int size()
    {
        if (rear >= front)
        {
            return (rear-front+1);
        }
        else
        {
            return ((max-front) + (rear+1));
        }
    }

    public void display()
    {
        /*
        if (isEmpty())
        {
            System.out.println("Empty queue");
            return;
        }
        */
        System.out.print("Queue: ");
        for (int i = front; i < max; i++)
        {
            System.out.print(arr[i] + " ");
        }
        if (!(rear >= front))
        {
            for (int i = 0; i < rear+1; i++)
            {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}

class rough
{
    public static void main(String args[])
    {
        Queue q = new Queue(5);

        q.display();

        q.insert(10);
        q.insert(24);
        q.insert(13);
        q.insert(11);
        q.insert(19);
        q.insert(29);

        System.out.println(q.rear + " " + q.front);

        q.display();

        q.delete();
        q.delete();
        q.delete();

        q.display();

        q.insert(30);
        q.insert(35);

        q.display();
    }
}
