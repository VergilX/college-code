import java.io.*;
import java.util.Scanner;

class Link
{
    private int data;
    public Link next;

    public Link(int d) {
        data = d;
        next = null;
    }

    public int getdata()
    { return data; }
}

class Queue
{
    public Link first;
    public Link last;

    public Queue()
    { first = last = null; }

    public void insertfirst(int d)
    {
        Link nl = new Link(d);

        if (first == null)
        { first = last = nl; return; }

        nl.next = first;
        first = nl;
        System.out.println("Inserted!");
    }

    public void insertlast(int d)
    {
        Link nl = new Link(d);

        if (first == null)
        {
            first = nl;
            last = nl;
            return;
        }
        last.next = nl;
        last = nl;
    }

    public void deletefirst()
    {
        if (first == null)
        {
            System.out.println("Empty");
            return;
        }

        Link temp = first;
        first = first.next;
        temp.next = null;
        System.out.println("Deleted!");
    }

    public void deletelast()
    {
        if (first == null)
        {
            System.out.println("Empty");
            return;
        }

        if (first.next == null)
        {
            first = null;
            last = null;
            return;
        }

        Link cur = first;
        while (cur.next.next != null)
        { cur = cur.next; }
        last = cur;
        last.next = null;
    }

    public void insertafterkey(int key, int d)
    {
        Link nl = new Link(d);

        Link cur = first;
        if (cur == null)
        {
            System.out.println("Empty");
            return;
        }

        while (cur != null)
        {
            if (key == cur.getdata())
            {
                nl.next = cur.next;
                cur.next = nl;
                return;
            }

            cur = cur.next;
        }

        System.out.println("Key not found!");
    }

    public void display()
    {
        if (first == null) {
            System.out.println("empty");
        }

        else {
            Link cur = first;

            System.out.print("\nQueue: ");
            while (cur.next != null)
            {
                System.out.print(cur.getdata() + " ==> ");
                cur = cur.next;
            }
            System.out.println(cur.getdata());
        }
    }
}

public class Queuepgm
{
    public static void main(String args[])
    {
        Queue ll = new Queue();
        Scanner sc = new Scanner(System.in);
        int ch = 0;

        while (ch != 4) {
            System.out.print("MENU OPTIONS:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter choice: ");
            ch = sc.nextInt();

            if (ch == 1) {
                System.out.print("Enter input: ");
                int a = sc.nextInt();

                ll.insertlast(a);
            }

            else if (ch == 2) {
                ll.deletefirst();
            }

            else if (ch == 3) {
                ll.display();
            }

            else if (ch == 4) {
                System.out.println("Terminating program");
            }

            else {
                System.out.println("Bad choice there :(");
            }
        }
    }
}
