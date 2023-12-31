import java.io.*;
import java.util.Scanner;

class Link
{
    private int data;
    public Link next;
    public Link prev;

    public Link(int data) {
        this.data = data;
    }

    public int getdata()
    { return data; }
}

class Deque
{
    public Link first;
    public int length;

    public Deque() {
        first = null;
        length = 0;
    }
    
    public void insertAtPos(int pos, int data) {
        Link nl = new Link(data);
        int count = 1;
        Link cur = first;

        if (pos == 1) {
            // If not the starting node set prev
            if (first != null)
                first.prev = nl;

            nl.next = first;
            System.out.println("Hello");
            first = nl;
            System.out.println("Inserted!");
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
                    
                    nl.prev = cur;
                    System.out.println("Inserted!");
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
            
        else {
            Link cur = first;
            int count = 0;
            // System.out.println(cur.getdata());

            while (cur.next != null) {
                if (count+1 == pos) {
                    System.out.println("I'm in boiiiiiiiii " + first);
                    cur.next = cur.next.next;
                    --length;

                    return;
                }
                cur = cur.next;
                ++count;
            }

            // If it is at the end
            if (pos == length+1) {
                System.out.println(cur.getdata());
                cur = cur.prev;
                System.out.println(cur.getdata());
                cur.next = null;
            }
        }
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

class Dequepgm
{
    public static void main(String args[]) {
        Deque d = new Deque();
        Scanner sc = new Scanner(System.in);
        int ch = 0;

        while (ch != 6) {
            System.out.print("MENU OPTIONS:\n1. Insert front\n2. Insert rear\n3. Delete front\n4. Delete rear\n5. Display\n6. Exit\nEnter your choice: ");
            ch = sc.nextInt();

            if (ch == 1) {
                System.out.print("Enter data: ");
                int a = sc.nextInt();

                d.insertAtPos(1, a);
            }
            else if (ch == 2) {
                System.out.print("Enter data: ");
                int a = sc.nextInt();

                d.insertAtPos(d.length+1, a);
            }
            else if (ch == 3) {
                d.deletePos(1);
            }
            else if (ch == 4) {
                System.out.println("Length of queue: " + d.length);
                d.deletePos(d.length+1);
            }
            else if (ch == 5) {
                d.display();
            }
            else if (ch == 6) {
                System.out.println("Terminating program");
            }
            else {
                System.out.println("Bad choice there :(");
            }
        }
    }
}
