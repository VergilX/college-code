; Hello World!
DATA SEGMENT
    MSG DB "Hello World!$"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    START:
        MOV AX, DATA
        MOV DS, AX

        MOV AH, 09H
        LEA DX, MSG
        INT 21H

    STOP:
        MOV AH, 4CH
        INT 21H
    
    CODE ENDS
END START
