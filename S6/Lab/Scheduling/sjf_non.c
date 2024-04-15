#include <stdio.h>

#define QUEUE_MAX 100

// Process size: 28
typedef struct process {
    int pid;
    int arrival_t;
    int burst_t;
    int turnaround_t;
    int waiting_t;
    int remaining_t;
    int completion_t;
}process;

typedef struct queue {
    process arr[QUEUE_MAX];
    process *front;
    process *end;
    int len;
}queue;


void qpush(queue *q, process p) {
    if (q->front == NULL) {
        q->arr[0] = p;
        q->front = q->end = &q->arr[0];
        q->len++;
        return;
    }

    q->end = q->end + 1;
    *(q->end) = p;
    q->len++;
}

process *qpop(queue *q) {
    if (q->front == NULL) {
        printf("Cannot pop more from queue\n");
        return NULL;
    }
    if (q->front == q->end) {
        // Starting over
        q->front = q->end = NULL;
    }

    process *p = q->front;
    q->front = q->front + 1;
    q->len--;
    return p;
}


void print_queue(queue q) {
    process *current = q.front;

    printf("queue: ");
    for (int i=0; i<q.len; ++i) {
        printf("%d ", current->pid);
        current = current+1;
    }
    printf("\n");
}


int main() {
    queue q;
    q.len = 0;

    process p1, p2, p3, p4;
    p1.pid = 1;
    p2.pid = 2;
    p3.pid = 3;
    p4.pid = 4;

    qpush(&q, p1);
    qpush(&q, p2);
    qpush(&q, p3);
    qpush(&q, p4);

    qpop(&q);
    qpop(&q);

    print_queue(q);

    return 0;
}
