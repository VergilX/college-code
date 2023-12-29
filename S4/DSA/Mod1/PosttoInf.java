import java.io.*;
import java.util.Scanner;

class Stack
{
    private int top;
    private int len;
    private int max;
    private int[] arr;

    public Stack(int max) {
        top = -1;
        len = 0;
        this.max = max;
        arr = new int[100];
    }

    public void push(int d) {
        if (!isFull()) {
            arr[++top] = d;
            ++len;
        }
    }
    
    public int pop() {
        if (!isEmpty()) {
            --len;
            return arr[top--];
        }

        else return 0;
    }

    public boolean isEmpty() {
        return (top == -1);
    }

    public boolean isFull() {
        return (top == max);
    }

    public void display() {
        if (!isEmpty()) {
            System.out.println("\nStack:\n" + arr[len-1] + " (Top)");
            for (int i=len-2; i>=0; --i) {
                System.out.println(arr[i]);
            }
        }
    }

    public int peek() {
        if (!isEmpty())
            return arr[top];
        else return 0;
    }

}

class PosttoInf
{
    public static void priority(char c)
    {
        if (c == "^")
            return 3
        else if (c=="*" || c=="/")
            return 2;
        else return 1;
    }

    public static void main(String args[])
    {
        String post = new String();
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter postfix string: ");
        post = sc.nextLine();

        Stack s = new Stack(5);
        for (int i=0; post[i] != post.length(); ++i) {
            char cur = arr[i];

            if (cur=="+" || cur=="-" || cur=="*" || cur=="/") {
                if (!s.isEmpty()) {
                    // Get priority and push/pop
                    int top = s.peek();

                    if (top=="+" || top=="-" || top=="*" || top=="/") {
                        if (priority(cur) > priority(s.peek()) {
                            
                        }
                    }
                }
                else s.push(cur);
            }

            else {
                s.push(cur);
            }
        }
    }
}

