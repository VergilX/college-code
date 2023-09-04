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

class AscQ
{
    public Link first;
    public int length;

    public AscQ()
    { first = null; }

    public void insertAtPos(int pos, int data) {
        Link nl = new Link(data);
        int count = 1;
        Link cur = first;

        if (pos == 1) {
            nl.next = first;
            first = nl;
            ++length;
        }

        else {
            while (cur != null) {
                
                if (count+1 == pos) {
                    if (cur.next != null) {
                        nl.next = cur.next;
                        cur.next = nl;
                    }
                    else {
                        cur.next = nl;
                    }
                    
                    ++length;
                    return;
                }
                cur = cur.next;
                ++count;
            }

            System.out.println("Position out of bounds");
        }

    }

    public void deletePos(int pos) {
        if (first == null)
            System.out.println("Empty queue");

        // If the given position is out of bounds
        else if (pos > length+1) {
            System.out.println("Given position is out of bounds");
        }

        else if (pos == 1) {
            first = first.next;
            --length;
        }

        // If it is at the end
        else if (pos == length+1) {
            Link cur = first;

            // If only single node
            if (cur.next == null) {
                first = null;
                return;
            }

            while (cur.next.next != null) {
                cur = cur.next;
            }
            cur.next = null;

        }
            
        else {
            Link cur = first;
            int count = 0;
            // System.out.println(cur.getdata());

            while (cur.next != null) {
                if (count+1 == pos) {
                    cur.next = cur.next.next;
                    --length;

                    return;
                }
                cur = cur.next;
                ++count;
            }

        }
    }

    public int find_pos(int d)
    {
        int pos = 0;
        Link cur = first;

        while (cur != null) {
            if (d > cur.getdata()) {
                cur = cur.next;
                ++pos;
            }
            else {
                break;
            }
        }

        return pos;
    }

    public void display() {
        if (first == null)
            System.out.println("Empty");

        else {
            Link cur = first;

            System.out.print("Queue: ");
            while (cur.next != null) {
                System.out.print(cur.getdata() + " ==> ");
                cur = cur.next;
            }

            System.out.println(cur.getdata());
        }
    }
}

class AscPriQ
{
    public static void main(String args[]) {
        AscQ d = new AscQ();
        Scanner sc = new Scanner(System.in);
        int ch = 0;

        while (ch != 4) {
            System.out.print("MENU OPTIONS:\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter your choice: ");
            ch = sc.nextInt();

            if (ch == 1) {
                System.out.print("Enter data: ");
                int a = sc.nextInt();

                int pos = d.find_pos(a);
                d.insertAtPos(pos+1, a);
            }
            else if (ch == 2) {
                d.deletePos(1);
            }
            else if (ch == 3) {
                d.display();
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
