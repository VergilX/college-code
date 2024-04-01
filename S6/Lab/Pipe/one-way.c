/*
    One-way pipe
    
    Abhinand D Manoj
    CS A
    20221002
 
*/
 
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
 
int main(void)
{
    int pfd;
    int n;
    
    printf("Enter number of numbers: ");
    scanf("%d", &n);
    
    int numbers[n];
    
    // Create pipe
    int pipefd[2];
    if (pipe(pipefd) == -1) {
        fprintf(stderr, "Pipe creation error\n");
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
        read(pipefd[0], numbers, sizeof(int)*n);
        
        // Print numbers
        printf("Child process(%d):\n", getpid());
        for (int i=0; i<n; ++i) {
            printf("%d\n", numbers[i]);
        }
        
        close(pipefd[0]);
    }
    // Parent process
    else {
        printf("Parent process(%d):\n", getpid());
        for (int i=0; i<n; ++i) {
            printf("Enter number %d: ", i+1);
            scanf("%d", &numbers[i]);
        }
        
        // Write to pipe after closing read end
        close(pipefd[0]);
        
        write(pipefd[1], numbers, sizeof(int)*n);
        
        close(pipefd[1]);
    }
 
}
