DATA SEGMENT
    INP1 DB "Enter first number: $"
    INP2 DB "Enter second number: $"
    OUTPUT DB "Output: $"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    PRINT PROC
        ; Assume content stored in DX
        MOV AH, 09H
        INT 21H
        RET
    PRINT ENDP

    PUTCHAR PROC
        ; Assume stored in DL
        MOV AH, 02H
        INT 21H  
        RET
    PUTCHAR ENDP

	DISPLAY PROC
		
		MOV CX,9
		CMP CX,BX
		JC TWO
		
	ONE:	MOV AX,BX
		ADD AX,48
		CALL PRINT
		JMP EEND
		
	TWO:
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
		CALL PUTCHAR
		
		
	EEND:
		
		RET
    DISPLAY ENDP

    INPUT PROC
        ; First number
        LEA DX, INP1
        CALL PRINT

        MOV AH, 01H
        INT 21H
        MOV BL, AL
        INT 21H
        MOV BH, AL

        ; Second number
        LEA DX, INP2
        CALL PRINT

        MOV AH, 01H
        INT 21H
        MOV CL, AL
        INT 21H
        MOV CH, AL

        ; Converting to decimal
        SUB BL, 48
        SUB BH, 48
        SUB CL, 48
        SUB CH, 48

        ; Correcting first number
        MOV AL, 10
        MUL BL
        MOV BL, AL
        ADD BL, BH

        ; Correcting second number
        MOV AL, 10
        MUL CL
        MOV CL, AL
        ADD CL, CH

        RET
    INPUT ENDP

    START:
        MOV AX, DATA
        MOV DS, AX

        CALL INPUT

        MOV AL, CL
        MUL BL
        MOV BX, AX
        ; Result in BX

        ; Converting back to ASCII
        ; ADD BH, 48
        ; ADD BL, 48
                    
        LEA DX, OUTPUT
        CALL PRINT
        
        CALL DISPLAY
    STOP:
        MOV AH, 4CH
        INT 21H
CODE ENDS
END START
