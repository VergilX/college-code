#include <iso646.h>
#include <stdio.h>
#include <stdlib.h>

#define QUEUE_MAX 100
#define TIME_MAX 1000
#define BURST_CAP 10000

typedef struct process {
    int pid;
    int arrival_t;
    int burst_t;
    int turnaround_t;
    int waiting_t;
    int remaining_t;
    int completion_t;
}process;


int input_proc(process arr[]) {
    int n;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i=0; i<n; ++i) {
        printf("\n==> proc %d\n", i+1);
        printf("Arrival time: ");
        scanf("%d", &arr[i].arrival_t);
        printf("Burst time: ");
        scanf("%d", &arr[i].burst_t);

        arr[i].pid = i;
        arr[i].waiting_t = 0;
        arr[i].remaining_t = arr[i].burst_t;
        arr[i].completion_t = 0;
        arr[i].turnaround_t = 0;
    }

    return n;
}


int proc_comp_arrival_t(const void *p1, const void *p2) {
    const process *proc1 = (const process *)p1;
    const process *proc2 = (const process *)p2;

    return (proc1->arrival_t - proc2->arrival_t);
}


void update_except(process input[], int n, process *p, int time) {
    for (int i = 0; i < n; ++i) {
        if ((input[i].pid!=p->pid) && (input[i].arrival_t<time+p->burst_t) && (input[i].remaining_t>0)) {
            int subtract = input[i].arrival_t > time ? (input[i].arrival_t-time) : 0;
            input[i].waiting_t += p->burst_t - subtract;
        }
    }
}


void calculate_data(process arr[], int n, int time) {
    for (int i=0; i<n; ++i) {
        arr[i].turnaround_t = arr[i].waiting_t + arr[i].burst_t;
        arr[i].completion_t = arr[i].arrival_t + arr[i].turnaround_t;
    }
}


void print_process_data(process arr[], int n) {
    printf("ProcessID\t\tArrivalTime\t\tBurstTime\t\tTurnaroundTime\t\tWaitingTime\t\tCompletionTime\n");

    for (int i=0; i<n; ++i) {
        printf("%9d\t\t%11d\t\t%9d\t\t%14d\t\t%11d\t\t%14d\n", arr[i].pid, arr[i].arrival_t, arr[i].burst_t, arr[i].turnaround_t, arr[i].waiting_t, arr[i].completion_t);
    }

    float avgTAT, avgWT;
    int sumTAT = 0;
    int sumWT = 0;
    for (int i=0; i<n; ++i) {
        sumTAT += arr[i].turnaround_t;
        sumWT += arr[i].waiting_t;
    }

    printf("Average waiting time: %f\n", (float)sumWT/n);
    printf("Average turnaround time: %f\n", (float)sumTAT/n);
}

int main(void)
{
    process input[QUEUE_MAX];
    int n = input_proc(input);
    int completed = 0;

    // Sorting via arrival time
    qsort(input, n, sizeof(process), proc_comp_arrival_t);

    process min_proc;
    min_proc.pid = -1;
    min_proc.arrival_t = 0;
    min_proc.burst_t = BURST_CAP;

    int time = 0;
    while (completed != n) {
        process *min = &min_proc;

        for (int i=0; i<n; ++i) {
            if ((input[i].arrival_t<=time) && (input[i].remaining_t>0)) {
                if (input[i].burst_t < min->burst_t) {
                    min = &input[i];
                }
                else if (input[i].burst_t == min->burst_t) {
                    if (input[i].arrival_t < min->arrival_t) {
                        min = &input[i];
                    }
                }
            }
        }

        // If minimum is found
        if (min->pid != -1) {
            completed++;
            min->remaining_t = 0;
            update_except(input, n, min, time);
            time = time + min->burst_t;
        } else ++time;
    }


    calculate_data(input, n, time);
    print_process_data(input, n);

    return 0;
}
