/*
    Two-way pipe 1
    
    Abhinand D Manoj
    CS A
    20221002
 
*/
 
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
bool is_prime(int);
 
int main(void)
{
    int pfd;
    int n;
    
    printf("Enter number of numbers: ");
    scanf("%d", &n);
    
    int numbers[n];
    
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
        read(pipefd[0], numbers, sizeof(int)*n);
        
        // Close first pipe
        close(pipefd[0]);
        
        // Use second pipe to send data back to parent
        close(pipefd2[0]);
        for (int i=0; i<n; ++i) {
            if (is_prime(numbers[i])) {
                write(pipefd2[1], &numbers[i], sizeof(int));
            }
        }
        
        printf("\nChild process(%d): Prime numbers calculated and sent to pipe\n", getpid());
        
        // Using delimiter as 0
        // write(pipefd2[1], 0, sizeof(int));
        close(pipefd2[1]);
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
        
        // Wait until child is done
        wait(NULL);
        
        int num;
        close(pipefd2[1]);
        printf("\nParent process(%d), prime numbers:\n", getpid());
        // Read from second pipe and print (delimiter: 0)
        while (read(pipefd2[0], &num, sizeof(int)) > 0) {
            printf("%d\n", num);
        }
        
        close(pipefd2[0]);
    }
}
 
 
bool is_prime(int n) {
    bool prime = true;
    
    for (int i=2; i<n/2+1; ++i) {
        if (n%i == 0) {
            prime = false;
            break;
        }
    }
    
    if (prime)
        return true;
    return false;
}
