import java.io.*;
import java.util.Scanner;

class Node
{
    public int data;
    public Node lchild;
    public Node rchild;
    public boolean rthread;

    public Node(int d)
    {
        data = d;
        lchild = rchild = null;
        rthread = false;
    }

    public void display()
    {
        System.out.print(data + " ");
    }
}

class Tree
{
    public Node root;

    public Tree() {}

    public Tree(Node a)
    { root = a; }

    public void insert(int d)
    {
        Node n = new Node(d);

        if (root == null) {
            root = n;
            return;
        }

        Node cur = root;
        while (true)
        {
            if (d >= cur.data) {
                if (cur.rchild == null) {
                    cur.rchild = n;
                    cur.rthread = false;

                    System.out.println("Inserted: " + cur.rchild.data + cur.rchild + " " + cur.rthread);
                    break;
                }
                cur = cur.rchild;
            }
            else {
                if (cur.lchild == null) {
                    n.rthread = true;
                    n.rchild = cur;
                    cur.lchild = n;

                    System.out.println("Inserted: " + cur.lchild.data + cur.lchild + " " + cur.rthread);
                    System.out.println("Inorder successor: " + cur.lchild.rchild.data);
                    break;
                }
                cur = cur.lchild;
            }
        }
    }
    
    public void inorder(Node r)
    {
        Node p = r;

        while (p != null)
        {
            if (p.lchild != null) {
                p = p.lchild;
            }
            else {
                if (p.rthread) { // Thread is present
                    Node local = p;
                    p.display();
                    p = p.rchild;
                    p.display();
                    if (p.rchild != local) {
                        p = p.rchild;
                    }
                    else
                        p = local.rchild;
                    break;
                }
                else {
                    p.display();
                    p = p.rchild;
                }
            }
        }
    }

    public void display()
    {
        if (root == null) {
            System.out.println("Empty tree");
            return;
        }

        // Non-recursive threaded traversal
        inorder(root);
    }

    public void search(int d)
    {
        Node cur = root;

        while (cur != null)
        {
            if (d > cur.data) {
                cur = cur.rchild;
            }
            else if (d < cur.data) {
                cur = cur.lchild;
            }
            else {
                System.out.println("Element found!");
                return;
            }
        }

        System.out.println("Element not found :( ");
    }
}

class threaded
{
    public static void main(String args[])
    {
        Tree t = new Tree();
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int curno;

        for (int i=0; i<n; ++i) {
            System.out.print("Enter number: ");
            curno = sc.nextInt();
            t.insert(curno);
        }

        t.display();
    }
}



