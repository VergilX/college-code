#include <stdbool.h>
#include <stdio.h>

#define QUEUE_MAX 10

typedef struct process {
	int pid;
	int arrival_t;
	int burst_t;
	int turnaround_t;
	int waiting_t;
	int completion_t;
} process;

void sort_by_arrival_t(process arr[], int n);
void print_process_data(process arr[], int n);
float AvgWaitingTime(process arr[], int n);
float AvgTurnaroundTime(process arr[], int n);

int main(void) {
	// Inputs
	process inputs[QUEUE_MAX];
	
	int n;
	printf("Enter number of processes: ");
	scanf("%d", &n);

	for (int i=0; i<n; ++i) {
		process p;
		printf("Process %d:\n", i);
		printf("Enter pid: ");
		scanf("%d", &p.pid);
		printf("Enter arrival time: ");
		scanf("%d", &p.arrival_t);
		printf("Enter burst time: ");
		scanf("%d", &p.burst_t);

		p.turnaround_t = p.waiting_t = p.completion_t = 0;
		inputs[i] = p;
		printf("\n");
	}

	sort_by_arrival_t(inputs, n);

	// Logic
    inputs[0].completion_t = inputs[0].turnaround_t = inputs[0].burst_t;
	for (int i=1; i<n; ++i) {
		int start_time = inputs[i-1].completion_t;
		if (inputs[i].arrival_t > start_time)
			start_time = inputs[i].arrival_t;
	
		inputs[i].waiting_t = start_time - inputs[i].arrival_t;
		inputs[i].turnaround_t = inputs[i].burst_t + inputs[i].waiting_t;
		inputs[i].completion_t = inputs[i].arrival_t + inputs[i].turnaround_t;
	}

	print_process_data(inputs, n);

    printf("Average waiting time: %f\n", AvgWaitingTime(inputs, n));
    printf("Average turnaround time: %f\n", AvgTurnaroundTime(inputs, n));
}

void sort_by_arrival_t(process arr[], int n) {
	// Bubble sort
	for (int i=0; i<n; ++i) {
		bool swapped = false;

		for (int j=0; j<n-i-1; ++j) {
			if (arr[j].arrival_t > arr[j+1].arrival_t) {
				// Swapping
				process temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
				swapped = true;
			}
		}

		if (!swapped)
				break;
	}
}


void print_process_data(process arr[], int n) {
	printf("ProcessID\t\tArrivalTime\t\tBurstTime\t\tTurnaroundTime\t\tWaitingTime\t\tCompletionTime\n");
	
	for (int i=0; i<n; ++i) {
		printf("%9d\t\t%11d\t\t%9d\t\t%14d\t\t%11d\t\t%14d\n", arr[i].pid, arr[i].arrival_t, arr[i].burst_t, arr[i].turnaround_t, arr[i].waiting_t, arr[i].completion_t);
	}
}


float AvgWaitingTime(process arr[], int n) {
    float sum = 0.0;

    for (int i=0; i<n; ++i) {
        sum += arr[i].waiting_t;
    }

    return (sum / n);
}


float AvgTurnaroundTime(process arr[], int n) {
    float sum = 0.0;

    for (int i=0; i<n; ++i) {
        sum += arr[i].turnaround_t;
    }

    return (sum / n);
}
