DATA SEGMENT
	MSG1 DB "Enter first string: $"
	MSG2 DB "Enter second string: $"
	MSG3 DB "Result: $"
DATA ENDS

; Conventions used:
; BX -> address of first string
; DI -> address of second string
; SI -> temporary address register

CODE SEGMENT
	ASSUME CS:CODE, DS:DATA

	;	read char kbd(output->AL)
	readChar PROC
		MOV AH, 01H
		INT 21H
		RET
	readChar ENDP

	;	write char screen(input->DL)
	writeChar PROC
		MOV AH, 02H
		INT 21H
		RET
	writeChar ENDP

	;	read string mem->screen(start_addr->SI, delimiter->'\r')
	readStringFromMem PROC
		CHAR_LOOP:
			MOV DL, [SI]
			CMP DL, 13 ; don't read \r
			JE CHAR_STOP

			CALL writeChar
			INC SI
			JMP CHAR_LOOP

		CHAR_STOP:
			RET
	readStringFromMem ENDP

	;	write string kbd->mem(start_addr->SI, delimiter->'\r')
	writeStringToMem PROC
		WRITE_MEM_LOOP:
			CALL readChar

			MOV [SI], AL
			CMP AL, 13 ; have to write \r
			JE WRITE_MEM_STOP
			INC SI
			JMP WRITE_MEM_LOOP

		WRITE_MEM_STOP:
			RET
	writeStringToMem ENDP

	;	print string(address->DX)
	printString PROC
		MOV AH, 09H
		INT 21H
		RET
	printString ENDP

	START:
		MOV AX, DATA
		MOV DS, AX

		;	store addresses according to convention
		MOV BX, 1000H
		MOV DI, 2000H

		;	print(Enter first string:)
		LEA DX, MSG1
		CALL printString

		;	read str1 and write to mem
		MOV SI, BX
		CALL writeStringToMem

		;	print("Enter second string: ")
		LEA DX, MSG2
		CALL printString

		;	read str2 and write to mem
		MOV SI, DI
		CALL writeStringToMem

		;	print("Result is: ")
		LEA DX, MSG3
		CALL printString

		;	concat
		MOV SI, BX
		CALL readStringFromMem
		MOV SI, DI
		CALL readStringFromMem

	STOP:
		MOV AH, 4CH
		INT 21H

	CODE ENDS
END START

