import java.io.*;
import java.util.Scanner;

class Stack
{
    private int max;
    private int top;
    private int length;
    private char[] arr;

    public Stack(int max) {
        this.max = max;
        top = -1;
        length = 0;
        arr = new char[max];
    }

    public void push(char d)
    {
        if (!isFull()) {
            arr[++top] = d;
            ++length;
        }
        else {
            System.out.println("Stack is full!");
        }
    }

    public boolean pop() 
    {
        if (!isEmpty()) {
            System.out.println("Popped element: " + arr[top]);
            --length;
            --top;
            return true;
        }
        return false;
    }

    public boolean isFull() {
        return (top == max);
    }

    public boolean isEmpty() {
        return (top == -1); 
    }

    public void display()
    {
        if (!isEmpty()) {
            System.out.println(arr[top] + " (top)");
            for (int i=top-1; i>=0; ++i) {
                System.out.println(arr[i]);
            }
        }
        else {
            System.out.println("Stack is empty~");
        }
    }
}

class balanceparanthesis
{
    public static void main(String args[])
    {
        String str;
        int n;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter maximum length of string: ");
        n = sc.nextInt();
        System.out.print("Enter string: ");
        str = sc.next();

        Stack s = new Stack(n);

        for (int i=0; i<n; ++i)
        {
            if (str.charAt(i) == '(') {
                s.push('(');
            }
            else if (str.charAt(i) == ')') {
                if (!s.pop()) {
                    System.out.println("String is not balanced!");
                    return;
                }
            }
        }

        // After iterating through the string, if there are any left
        if (s.isEmpty()) {
            System.out.println("String is balanced!");
        }
        else {
            System.out.println("String is not balanced");
        }
    }
}
