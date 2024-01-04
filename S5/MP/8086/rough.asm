DATA SEGMENT
    MSG DB "Hello World$"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

    START:
        MOV AX, DATA
        MOV DS, AX

        MOV BX, 1000H
        MOV SI, 2000H

        MOV DX, 0002H
        MOV [BX], DX
        MOV [SI], DX
        MOV AX, [SI]

        CMP [BX], AX
        JZ PRINT
    STOP:
        MOV AH, 4CH
        INT 21H
    PRINT:
        LEA DX, MSG
        MOV AH, 09H
        INT 21H
        JMP STOP

CODE ENDS
END START
