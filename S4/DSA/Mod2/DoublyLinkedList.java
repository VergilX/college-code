import java.io.*;
import java.util.Scanner;

class Link
{
    private int data;
    public Link next;
    public Link prev;

    public Link(int d)
    {
        data = d;
        next = prev = null;
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
        first.prev = nl;
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
        nl.prev = last;
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
        first.prev = null;
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

        Link temp = last;
        last = last.prev;
        temp.prev = null;
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
                cur.next.prev = nl;
                nl.prev = cur;
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
            System.out.print(cur.getdata() + " <==> ");
            cur = cur.next;
        }
        System.out.println(cur.getdata());
    }
}

public class DoublyLinkedList
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

        ll.display();
        
        ll.insertafterkey(10, 0);
        ll.deletefirst();

        ll.display();
    }
}
