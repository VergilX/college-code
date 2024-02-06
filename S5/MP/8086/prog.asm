DATA SEGMENT
    INP1 DB "x: $"
    INP2 DB "y: $"
    OUTPUT DB "Ans: $"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

    INPUT PROC
        MOV AH, 01H
        INT 21H

        MOV BL, AL

        MOV AH, 01H
        INT 21H

        MOV CL, AL

        ; Convert to decimal
        SUB BL, 48
        SUB CL, 48
        RET
    INPUT ENDP

    PRINT PROC
        MOV DL, AL
        MOV AH, 02H
        INT 21H
        RET
    PRINT ENDP

    DISPLAY PROC
        ; Assuming result in BX
        CMP BX, 9
        JC ONE
        JMP MORE

        ONE:
            ADD BX, 48
            MOV AL, BL
            CALL PRINT
            RET

        MORE:
            MOV CL,10 ;8 BIT NUMBER
            MOV AX,BX
            DIV CL
            
            
            MOV CH,AH
            SUB AH,AH
            MOV BX,AX
            
            PUSH CX
            CALL DISPLAY
            POP CX
            
            MOV AL,CH
            ADD AL,48
            CALL PRINT
            ; MOV AX, BX
            ; MOV CL, 10
            ; DIV CL

            ; PUSH AX
            ; CALL DISPLAY
            ; POP AX

            ; MOV AL, AH
            ; ADD AL, 48
            ; CALL PRINT
            ; RET
    DISPLAY ENDP

    START:
        MOV AX, DATA
        MOV DS, AX
        
        CALL INPUT
        ; Inputs in BL, CL

        ; (x+y)(x-y)
        MOV AL, BL
        ADD AL, CL
        MOV AH, BL
        SUB AH, CL
        MUL AH

        MOV BX, AX
        CALL DISPLAY

    STOP:
        MOV AH, 4CH
        INT 21H

CODE ENDS
END START
