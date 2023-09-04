import java.io.*;
import java.util.Scanner;

class CQ
{
    private int f, r, max;
    private int[] arr;

    CQ(int s)
    {
        max = s;
        r = -1;
        f = 0;
        arr = new int[max];
    }

    public boolean isFull()
    {
        if ((r+2) % max == f)
            return true;

        return false;
    }

    public boolean isEmpty()
    {   
        if ((r+1) % max == f)
            return true;

        return false;
    }

    public void insert(int d)
    {
        if (isFull()) {
            System.out.println("Queue is full!");
            return;
        }

        // If the rear has reached the max
        if (r == max-1) {
            r = -1;
        }
        arr[++r] = d;
    }

    public void delete()
    {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return;
        }

        // If front has reached the beginning
        if (f == max-1) {
            System.out.println("Removed element: " + arr[f]);
            f = 0;
        }
        else
            System.out.println("Removed element: " + arr[f++]);
    }

    public void display()
    {
        if (isEmpty()) {
            System.out.println("Queue is Empty!");
            return;
        }

        if (r >= f) {
            for (int i=f; i<=r; ++i) {
                System.out.println(arr[i] + " i=" + i);
            }
        }
        else {
            for (int i=f; i<max; ++i) {
                System.out.println(arr[i] + " i=" + i);
            }
            for (int i=0; i<=r; ++i) {
                System.out.println(arr[i] + " i=" + i);
            }
        }
    }
}

class Cqueue
{
    public static void main(String args[])
    {
        CQ q = new CQ(5);

        q.insert(1);
        q.insert(2);
        q.insert(3);
        q.insert(4);
        q.display();

        q.delete();
        q.display();
        q.insert(0);
        System.out.println('\n');

        q.display();
        q.delete();
        System.out.println('\n');

        q.insert(10);
        q.display();
    }
}
