import java.io.*;
import java.util.Scanner;

class Node
{
    public int data;
    public Node lchild;
    public Node rchild;

    public Node(int d)
    { data = d; }

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
                    break;
                }
                cur = cur.rchild;
            }
            else {
                if (cur.lchild == null) {
                    cur.lchild = n;
                    break;
                }
                cur = cur.lchild;
            }
        }
    }
    
    public void inorder(Node p)
    {
        if (p != null) {
            inorder(p.lchild);
            p.display();
            inorder(p.rchild);
        }
    }

    public void display()
    {
        if (root == null) {
            System.out.println("Empty tree");
            return;
        }

        // Recursive traversal
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

class tree
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



