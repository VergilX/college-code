import java.io.*;

class SelectionSort
{
    public static void swap(int[] arr, int pos1, int pos2)
    {
        int temp = arr[pos1];
        arr[pos1] = arr[pos2];
        arr[pos2] = temp;
    }
        
    public static void selectionsort(int[] arr, int n)
    {
        // pos -> Position to replace
        // min -> Position of minimum element

        int i, min, pos;
        i = min = pos = 0;

        while (pos != (n-1))
        {
            if (arr[i] < arr[min])
            {
                min = i;
            }
            if (i == n-1)
            {
                swap(arr, pos, min);
                min = ++pos;
                i = pos + 1;
            }
            else i++;
        }
    }

    public static void main(String args[])
    {
        int n = 10;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
        {
            arr[i] = n - i;
        }

        selectionsort(arr, n);

        for (int i = 0; i < n; i++)
        {
            System.out.print(arr[i] + " ");
        }
    }
}
