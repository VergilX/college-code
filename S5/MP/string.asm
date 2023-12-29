; Program to input a string and echo it
DATA SEGMENT
    MSG DB "Enter string: $"
    STRING DB 10 DUP('$')
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    START:
        MOV AX, DATA
        MOV DS, AX

        ; Display message
        MOV AH, 09H
        LEA DX, MSG
        INT 21H

        ; Loading SI with memory address of string
        LEA SI, STRING

        ; Input whole string in array
        INPUT:
            ; Get single character into AL
            CALL GETCHAR
            CMP AL, 0DH
            JZ OUTPUT
            MOV [SI], AL
            INC SI
            JMP INPUT


        OUTPUT:
            ; Print whole string to display
            LEA DX, STRING
            MOV AH, 09H
            INT 21H

    STOP:
        MOV AH, 4CH
        INT 21H

    GETCHAR PROC
        MOV AH, 01H
        INT 21H
        RET
    GETCHAR ENDP

    CODE ENDS
END START
