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
		ADD DL, 48
		MOV AH, 02H
		INT 21H

		RET
	OUTPUT ENDP

	OUTPUT_SEP PROC
		MOV DL, ','
		INT 21H
		RET
	OUTPUT_SEP ENDP

	; Assuming number is in CL
	STACK_LOGIC PROC
		CMP CL, 09H
		JS ONE
		
		TWO:
			; BL containss the value OA
			MOV AL, CL
			MOV AH, 00H
			DIV BL

			PUSH AX
			MOV CL, AL
			CALL STACK_LOGIC
			POP AX
			MOV DL, AH
			CALL OUTPUT
			RET

		ONE:
			MOV DL, CL
			CALL OUTPUT

		RET
	STACK_LOGIC ENDP
		
	START:
		MOV AX, DATA
		MOV DS, AX

		; Immediate value for division
		MOV BL, 10

		; Get input and print as first number
		CALL INPUT
		MOV DL, DH
		CALL OUTPUT
		CALL OUTPUT_SEP

		; Clear CH and add 2*DH to it
		MOV CH, 00H
		ADD CH, DH
		ADD CH, DH
		
		; Set BH = 9 ( counter )
		MOV BH, 09H
		
		MOV CL, CH
		OUTER_LOOP:
			; Checking if the answer is one digit or two digit
			CMP CL, 0AH
			JS ONE_DIGIT
			JMP TWO_DIGIT

			ONE_DIGIT:
				MOV DL, CL
				CALL OUTPUT
				CALL OUTPUT_SEP
				JMP OUTER_LOOP_END
				
			TWO_DIGIT:
				CALL STACK_LOGIC
				CALL OUTPUT_SEP
				JMP OUTER_LOOP_END

			OUTER_LOOP_END:
				ADD CH, DH
				MOV CL, CH
				SUB BH, 01H

				CMP BH, 00H
				JNZ OUTER_LOOP

	STOP:
		MOV AH, 4CH
		INT 21H

CODE ENDS
END START
