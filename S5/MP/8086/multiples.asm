DATA SEGMENT
	INP DB "Enter character: $"
DATA ENDS

CODE SEGMENT
	ASSUME CS:CODE, DS:DATA

	; Input number and store in DH
	; after conversion to hex
	INPUT PROC
		; We don't have to deal with hex
		; digits (A-F) as we are only 
		; taking inputs 0-9
		MOV AH, 01H
		INT 21H

		SUB AL, 30H
		MOV DH, AL

		; printing carriage return
		MOV DL, 20H
		MOV AH, 02H
		INT 21H
		RET
	INPUT ENDP

	; Output character from DL after conversion
	; to ascii and '=' after
	OUTPUT PROC
		; We don't have to deal with hex digits as
		; as we are taking individual digits
		ADD DL, 30H 

		MOV AH, 02H
		INT 21H

		MOV DL, '='
		INT 21H
		RET
	OUTPUT ENDP
		
	START:
		MOV AX, DATA
		MOV DS, AX

		; Get input and print as first number
		CALL INPUT
		MOV DL, DH
		CALL OUTPUT

		; Clear CH and add 2*DH to it
		MOV CH, 00H
		ADD CH, DH
		ADD CH, DH
		
		; Set BH = 9-1 ( counter )
		MOV BH, 08H
		
		MOV CL, CH
		OUTER_LOOP:
			; Checking if the answer is one digit or two digit
			CMP CL, 09H
			JS ONE_DIGIT

			ONE_DIGIT:
				MOV DL, CL
				CALL OUTPUT
				JMP OUTER_LOOP_END
				
			TWO_DIGIT:
				JMP OUTER_LOOP_END

			OUTER_LOOP_END:
				ADD CL, DH
				SUB BH, 01H

				CMP BH, 00H
				JNZ OUTER_LOOP

	STOP:
		MOV AH, 4CH
		INT 21H

CODE ENDS
END START
