/*
    Two-way pipe 2

    Abhinand D Manoj
    CS A
    20221002

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define MAX_STR_LEN 1000

int is_palindrome(char str[]);


// Globals
int TRUE = 1;
int FALSE = 0;

int main(void)
{
    int pfd;
    char str[MAX_STR_LEN];
    int n;

    // Create first pipe
    int pipefd[2];
    if (pipe(pipefd) == -1) {
        fprintf(stderr, "Pipe creation error\n");
        exit(1);
    }

    int pipefd2[2];
    if (pipe(pipefd2) == -1) {
        fprintf(stderr, "Pipe 2 creation error\n");
        exit(1);
    }

    int p = fork();

    // Error
    if (p < 0) {
        printf("Fork failed\n");
        exit(1);
    }
    // Child process
    else if (p == 0) {
        // Read from pipe after closing write end
        close(pipefd[1]);
        read(pipefd[0], str, sizeof(char)*(n+1));

        // Close first pipe
        close(pipefd[0]);

        // Check if palindrome and send back result
        close(pipefd2[0]);
        if (is_palindrome(str)) {
            write(pipefd2[1], &TRUE, sizeof(int));
        } else {
            write(pipefd2[1], &FALSE, sizeof(int));
        }

        printf("\nChild process(%d): Calculated paldinrome and sent to pipe\n", getpid());

        close(pipefd2[1]);
    }
    // Parent process
    else {

        printf("Parent process(%d) request input:\n", getpid());
        printf("Enter string: ");
        scanf("%s", str);

        // printf("Parent process(%d):\n", getpid());

        // Write to pipe after closing read end
        close(pipefd[0]);

        write(pipefd[1], str, sizeof(char)*n);

        close(pipefd[1]);

        // Wait until child is done
        wait(NULL);

        close(pipefd2[1]);
        printf("\nParent process(%d), result: ", getpid());
        // Read from second pipe and print result
        int result;
        read(pipefd2[0], &result, sizeof(int));
        if (result) {
            printf("is palindrome\n");
        } else {
            printf("is not palindrome\n");
        }

        close(pipefd2[0]);
    }
}


int is_palindrome(char str[]) {
    int len = strlen(str);

    for (int i=0; i<len/2; ++i) {
        if (str[i] != str[len-(i+1)]) {
            return FALSE;
        }
    }

    return TRUE;
}
