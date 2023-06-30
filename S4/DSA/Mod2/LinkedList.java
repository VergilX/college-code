import java.io.*;
import java.util.Scanner;

class Link
{
    private int data;
    public Link next;

    public Link(int d)
    {
        data = d;
        next = null;
    }

    public int getdata()
    { return data; }
}

class DLinkList
{
    public Link first;
    public Link last;

    public DLinkList()
    { first = last = null; }

    public void insertfirst(int d)
    {
        Link nl = new Link(d);

        if (first == null)
        { first = last = nl; return; }

        nl.next = first;
        first = nl;
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
        Link cur = first;

        System.out.print("\nLinked List: ");
        while (cur.next != null)
        {
            System.out.print(cur.getdata() + " ==> ");
            cur = cur.next;
        }
        System.out.println(cur.getdata());
    }
}

public class LinkedList
{
    public static void main(String args[])
    {
        DLinkList ll = new DLinkList();

        ll.insertfirst(3);
        ll.insertfirst(4);
        ll.insertfirst(5);

        ll.insertlast(6);
        ll.insertlast(10);
        ll.insertlast(7);

        System.out.println(ll.last.getdata());
        ll.display();
        
        ll.insertafterkey(10, 0);

        ll.display();
    }
}
