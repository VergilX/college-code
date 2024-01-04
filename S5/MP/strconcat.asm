DATA SEGMENT

DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

    GETMEM PROC
        ; Assuming address in BX
        ; and storing result in AL
        MOV AL, [BX]
        RET
    GETMEM ENDP

    PUTMEM PROC
        ; Assuming character present in AL
        ; address in BX
        MOV [BX], AL
        RET
    PUTMEM ENDP

    PRINT PROC
        ; Assuming character present in AL
        MOV DL, AL
        MOV AH, 02H
        INT 21H
        RET
    PRINT ENDP

    START:
        MOV AX, DATA
        MOV DS, AX
        
        ; Accepting strings in locations 1000H and 2000H
        MOV BX, 1000H

        GET_FIRST_STRING:
            MOV AH, 01H
            INT 21H

            ; Character in AL
            CALL PUTMEM

            INC BX
            CMP AL, 0DH
            JNZ GET_FIRST_STRING

        MOV BX, 2000H
        GET_SECOND_STRING:
            MOV AH, 01H
            INT 21H

            ; Character in AL
            CALL PUTMEM

            INC BX
            CMP AL, 0DH
            JNZ GET_SECOND_STRING

        ; Concatenation
        MOV BX, 1000H
        MOV CX, 2000H
        STR1:
            CALL GETMEM
            ; If CR is reached
            CMP AL, 0DH
            JZ STR2
            ; CALL PRINT
            INC BX
            JMP STR1

        STR2:
            MOV DX, BX
            MOV BX, CX
            CALL GETMEM

            MOV BX, DX
            CALL PUTMEM
            INC BX
            INC CX

            CMP AL, 0DH
            JNZ STR2

        MOV BX, 1000H
        DISPLAY:

            CALL GETMEM

            CMP AL, 0DH
            JZ STOP

            CALL PRINT
            INC BX
            JMP DISPLAY

    STOP:
        MOV AH, 4CH
        INT 21H

CODE ENDS
END START
