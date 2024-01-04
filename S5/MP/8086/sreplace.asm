DATA SEGMENT
    INP1 DB "Enter string 1: $"
    INP2 DB "Enter string 2: $"
    INP3 DB "Enter new string: $"
    OUTPUT DB "Output: $"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA

    PUTMEM PROC
        MOV [BX], AL
        RET
    PUTMEM ENDP

    GETMEM PROC
        MOV AL, [BX]
        RET
    GETMEM ENDP

    PRINT PROC
        MOV AH, 02H
        INT 21H
        RET
    PRINT ENDP
    START:
        MOV AX, DATA
        MOV DS, AX

        MOV BX, 1000H
        ; Print message
        MOV AH, 09H
        LEA DX, INP1
        INT 21H

        FIRST_STRING:
            MOV AH, 01H
            INT 21H

            CALL PUTMEM
            INC BX
            CMP AL, 0DH
            JNZ FIRST_STRING

        MOV BX, 2000H
        ; Print message
        MOV AH, 09H
        LEA DX, INP2
        INT 21H

        SECOND_STRING:
            MOV AH, 01H
            INT 21H

            CALL PUTMEM
            INC BX
            CMP AL, 0DH
            JNZ SECOND_STRING

        MOV BX, 3000H
        ; Print message
        MOV AH, 09H
        LEA DX, INP3
        INT 21H
        THIRD_STRING:
            MOV AH, 01H
            INT 21H

            CALL PUTMEM
            INC BX
            CMP AL, 0DH
            JNZ THIRD_STRING
            
        ; Two pointers
        MOV BX, 1000H
        MOV SI, 2000H

        ; Print message
        MOV AH, 09H
        LEA DX, OUTPUT
        INT 21H
        PRINT_ANS:
            MOV CL, [BX]

            ; If they are the same
            CMP CL, [SI]
            JZ SAME
            JMP DIFF

            SAME:
                ; do stuff
                PUSH BX
                PUSH SI
                JMP ALOOP

                PRINTALL:
                    POP SI
                    POP BX
                    PRINTLOOP:
                        MOV DI, 3000H
                        MOV DL, [DI]
                        CMP DL, 0DH
                        JZ CONTINUE

                        CALL PRINT
                        INC DL
                        JMP PRINTLOOP

                ALOOP:
                    INC BX
                    INC SI
                    
                    MOV DL, [SI]
                    CMP DL, 0DH
                    JZ PRINTALL

                    CMP DL, [BX]
                    JZ ALOOP
                    POP SI
                    POP BX
                    JMP DIFF
                    
            DIFF:
                MOV DL, CL
                CALL PRINT

            CONTINUE:
                INC BX
                INC SI
                CMP CL, 0DH
                JZ STOP
                JMP PRINT_ANS

    STOP:
        MOV AH, 4CH
        INT 21H
CODE ENDS
END START
