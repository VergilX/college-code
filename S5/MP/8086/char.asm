; Program to echo character
DATA SEGMENT
    MSG DB "Enter char: $"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    START:
        ; Seting data segment and code segment
        MOV AX, DATA
        MOV DS, AX

        ; Display message
        MOV AH, 09H
        LEA DX, MSG
        INT 21H

        ; Input character
        MOV AH, 01H
        INT 21H
        MOV BL, AL

        ; Output character
        MOV DL, BL
        MOV AH, 02H
        INT 21H

    STOP:
        MOV AH, 4CH
        INT 21H
    CODE ENDS
END START
