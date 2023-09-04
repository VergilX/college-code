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
    
    public char peek()
    {
        return arr[top];
    }

    public char pop() 
    {
        if (!isEmpty()) {
            --length;
            return arr[top--];
        }
        return '~'; // Only for not getting error
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
class Infix_Postfix
{
    public static int priority(char a)
    {
        if (a == '^')
            return 3;

        else if (a=='*' || a=='/')
            return 2;

        else if (a=='+' || a=='-')
            return 1;

        return -1;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter string: ");
        String str = sc.next();
        Stack s = new Stack(str.length());
        
        for (int i=0; i<str.length(); ++i)
        {
            char c = str.charAt(i);

            if (c == '(')
                s.push(c);

            else if (c == ')') {
                while (s.peek() != '(') {
                    System.out.print(s.pop());
                }
                s.pop(); // Removing the (
            }

            else if (c=='+' || c=='-' || c=='*' || c=='/' || c=='^')
            {
                if (s.isEmpty()) {
                    s.push(c);
                }
                else if (priority(c) > priority(s.peek())) {
                    s.push(c);
                }
                else {
                    while (!s.isEmpty()) {
                        if (priority(c) <= priority(s.peek()))
                            System.out.print(s.pop());
                        else break;
                    }
                    s.push(c);
                }
            }

            else
            {
                System.out.print(c);
            }
        }

        // If there are any elements left in stack
        while (!s.isEmpty())
        {
            System.out.print(s.pop());
        }
        System.out.println();
    }
}
