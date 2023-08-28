import java.io.*;
import java.util.Scanner;

class Stack
{
    public int top;
    public int max;
    public int[] arr;
    public int length;

    public Stack(int max)
    {
        this.max = max;
        top = -1;
        length = 0;
        arr = new int[max];
    }

    public void push(int d) 
    {
        if (!isFull()) {
            arr[++top] = d;
            length++;
        }
        else {
            System.out.println("Stack is full");
        }
    }

    public int pop() 
    {
        if (!isEmpty()) {
            int pos;
            if ((pos=get_freq_pos()) != -1) {
                // Shift element after removing the element
                int temp = arr[pos];

                for (int i=pos; i<length-1; ++i)
                    arr[i] = arr[i+1];
                
                --length;
                return temp;
            }
        }

        System.out.println("Stack is full");
        return -1;
    }

    public boolean isFull()
    {
        return (max == length);
    }

    public boolean isEmpty() 
    {
        return (length == 0);
    }

    public int get_freq_pos()
    {
        int pos = -1;
        int max=0;
        int len=0;
        int new_max;
        int[] checked = new int[this.max];

        for (int i=0; i<length; ++i) {
            if (!is_in(checked, arr[i], len)) {
                System.out.print("Element being checked: " + arr[i]);
                new_max = 1;
                checked[len++] = arr[i];
                
                for (int j=i+1; j<length; ++j) {
                    if (arr[j] == arr[i]) {
                        ++new_max;
                    }
                }

                System.out.println(", Number of times repeated: " + new_max);
                if (new_max > max) {
                    max = new_max;
                    pos = i;
                }
            }
        }

        System.out.println("Popped position: " + pos);
        return pos;
    }

    public boolean is_in(int[] arr, int elem, int len)
    {
        for (int i=0; i<len; ++i) {
            if (arr[i] == elem) {
                return true;
            }
        }

        return false;
    }


    public void display()
    {
        System.out.println("Stack:\n" + arr[length-1] + " (top)");
        for (int i=length-2; i>=0; --i) {
            System.out.println(arr[i]);
        }
    }
}

class ModStack
{
    public static void main(String[] args)
    {
        Stack s = new Stack(5);

        s.push(1);
        s.push(2);
        s.push(3);
        s.push(1);
        s.push(1);
        
        s.display();

        System.out.println("Popped element is: " + s.pop());
        s.display();
        System.out.println("Popped element is: " + s.pop());
        s.display();
        System.out.println("Popped element is: " + s.pop());
        s.display();
    }
}
