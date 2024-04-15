#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define OTP_LEN 6

int main()
{
    int fd_parentTOchild[2];
    int fd_childTOparent[2];

    if (pipe(fd_parentTOchild) < 0) {
        fprintf(stderr, "pipe error: parent to child");
        exit(EXIT_FAILURE);
    }

    if (pipe(fd_childTOparent) < 0) {
        fprintf(stderr, "pipe error: child to parent");
        exit(EXIT_FAILURE);
    }

    pid_t p = fork();

    if (p < 0) {
        fprintf(stderr, "Process fork error");
        exit(EXIT_FAILURE);
    }
    else if (p == 0) {
        // Child process
        close(fd_parentTOchild[1]);
        char otp_from_parent[OTP_LEN+1];
        read(fd_parentTOchild[0], otp_from_parent, sizeof(char)*(OTP_LEN+1));
        close(fd_parentTOchild[0]);
        printf("Client==> Reading from pipe\n");

        printf("Client==> Received OTP: %s\n", otp_from_parent);
        char otp_to_send[OTP_LEN+1];
        printf("Enter OTP: ");
        scanf("%s", otp_to_send);
        otp_to_send[OTP_LEN] = '\0';

        printf("Client==> Sending to pipe...\n\n");
        close(fd_childTOparent[0]);
        write(fd_childTOparent[1], otp_to_send, sizeof(char)*(OTP_LEN+1));
        close(fd_childTOparent[1]);
    }
    else {
        // Parent process
        char OTP[OTP_LEN+1];
        
        printf("Bank==> Set OTP:\n");
        printf("Enter OTP to send: ");
        scanf("%s", OTP);
        OTP[OTP_LEN] = '\0';

        // Check for invalid OTP
        for (int i=0; i<OTP_LEN+1; ++i) {
            if (!isdigit(OTP[i])) {
                printf("Invalid OTP value\n");
                kill(0, SIGKILL);
                exit(EXIT_FAILURE);
            }
        }
        if (strlen(OTP) != OTP_LEN) {
            printf("Invalid OTP length\n");
            kill(0, SIGKILL);
            exit(EXIT_FAILURE);
        }

        printf("Bank==> Sending OTP to pipe\n");
        close(fd_parentTOchild[0]);
        write(fd_parentTOchild[1], OTP, sizeof(char)*(OTP_LEN+1));
        close(fd_parentTOchild[1]);

        printf("Bank==> Waiting for client to respond\n\n");
        wait(NULL);

        printf("Bank==> Reading client response from pipe\n");
        close(fd_childTOparent[1]);
        char otp_received_from_child[OTP_LEN+1];
        read(fd_childTOparent[0], otp_received_from_child, sizeof(char)*(OTP_LEN+1));
        close(fd_childTOparent[0]);

        printf("\nBank==> Validating OTP...\n");
        if (strcmp(OTP, otp_received_from_child) == 0) {
            printf("Transaction permitted\n");
        } else {
            printf("Transaction aborted\n");
        }
    }

    return 0;
}
