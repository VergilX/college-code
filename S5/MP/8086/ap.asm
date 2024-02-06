DATA SEGMENT
	MSG1 DB 13, 10, "a: $"
	MSG2 DB 13, 10, "d: $"
	MSG3 DB 13, 10, "n: $"
	MSG4 DB 13, 10, "Result: $"
	a DB ?
	d DB ?
	n DB ?
DATA ENDS

CODE SEGMENT
	ASSUME CS:CODE, DS:DATA

	;	kbd char input(stored->AL)
	inputChar PROC
		MOV AH, 01H
		INT 21H
		RET
	inputChar ENDP

	;	char to screen(input->DL)
	displayChar PROC
		MOV AH, 02H
		INT 21H
		RET
	displayChar ENDP

	;	get 8-bit number from kbd(stored->DL)
	inputNumber PROC
		CALL inputChar

		CALL decimalAsciiToHex

		; AX = AL * operand
		MUL BL ; BL is set as 10
		MOV DL, AL ; Result in AX, taking lower nibble

		CALL inputChar
		CALL decimalAsciiToHex
		ADD DL, AL
		RET
	inputNumber ENDP

	;	ascii->hex(input->AL, stored->AL)
	;	condition: no digit from A-F
	decimalAsciiToHex PROC
		SUB AL, 48
		RET
	decimalAsciiToHex ENDP

	;	hex->decimal(input->CX, output->screen)
	hexToDecimalAscii PROC
		CMP CX, 10
		JL ONE_DIGIT
		JMP MORE_THAN_ONE_DIGIT

		ONE_DIGIT:
			ADD CX, 48
			MOV DL, CL
			CALL displayChar
			RET

		MORE_THAN_ONE_DIGIT:
			; BL = 10 already
			MOV AX, CX
			DIV BL
			MOV CL, AL ; CL = quotient
			MOV CH, AH ; CH = remainder

			PUSH CX
			MOV CH, 00H
			CALL hexToDecimalAscii

			POP DX
			MOV DL, DH ; moving remainder
			ADD DL, 48
			CALL displayChar

		RET
	hexToDecimalAscii ENDP

	;	print to screen(address->DX)
	printString PROC
		MOV AH, 09H
		INT 21H
		RET
	printString ENDP

	START:
		MOV AX, DATA
		MOV DS, AX

		;	Temporary register: BL
		MOV BL, 10


		;	print(d: )
		LEA DX, MSG2
		CALL printString

		;	CH = d
		CALL inputNumber
		MOV CH, DL

		;	print(n: )
		LEA DX, MSG3
		CALL printString

		;	CL = n
		CALL inputNumber
		MOV CL, DL
		MOV AL, CL
		MOV AH, 00H

		;	(n-1)*d
		SUB CL, 01H
		MOV AL, CL
		MOV AH, 00H
		MUL CH ; result in AX
		MOV CX, AX

		;	print(a: )
		LEA DX, MSG1
		CALL printString

		;	a + (n-1)d
		CALL inputNumber
		MOV DH, 00H
		ADD CX, DX

		;	print(Result: )
		LEA DX, MSG4
		CALL printString

		call hexToDecimalAscii


	STOP:
		MOV AX, 4C00H
		INT 21H
CODE ENDS
END START
