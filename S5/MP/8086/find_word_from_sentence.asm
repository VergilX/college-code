DATA SEGMENT
	enterString DB 13, 10, "Enter string: $"
	enterWord DB 13, 10, "Enter word: $"
	final DB 13, 10, "Ans: $"
DATA ENDS

CODE SEGMENT
	ASSUME CS:CODE, DS:DATA

	;	kdb input(stored->AL)
	inputChar PROC
		MOV AH, 01H
		INT 21H
		RET
	inputChar ENDP

	;	screen output(input->DL)
	displayChar PROC
		MOV AH, 02H
		INT 21H
		RET
	displayChar ENDP

	;	print  string(address->DX)
	printString PROC
		MOV AH, 09H
		INT 21H
		RET
	printString ENDP

	;	write string to memory(input_addr->SI, delimiter->CR)
	writeStringToMem PROC
		CHAR_LOOP:
			CALL inputChar
			MOV [SI], AL

			CMP AL, 13
			JE CHAR_END
			INC SI
			JMP CHAR_LOOP

		CHAR_END:
			RET
	writeStringToMem ENDP

	;	read string mem->screen(input_addr->SI, delimiter->CR)
	readStringFromMem PROC
		DISPLAY_STRING_LOOP:
			MOV DL, [SI]
			CMP DL, 13
			JE DISPLAY_STRING_STOP
			CALL displayChar
			INC SI
			JMP DISPLAY_STRING_LOOP
		
		DISPLAY_STRING_STOP:
			RET
	readStringFromMem ENDP

	START:
		MOV AX, DATA
		MOV DS, AX

		;	string pointers
		MOV SI, 1000H

		;	print("Enter string: ")
		LEA DX, enterString
		CALL printString

		;	string->mem
		CALL writeStringToMem

		;	print("Enter word: ")
		LEA DX, enterWord
		CALL printString

		;	string->mem
		MOV SI, 2000H
		CALL writeStringToMem

		MOV SI, 1000H
		MOV DI, 2000H
		MOV CH, 00H

		;	word logic
		SENTENCE_TRAVERSE:
			WORD_LOOP:
				MOV BH, [SI]
				MOV BL, [DI]

				CMP BH, BL
				JE NEXT_CHAR

				CMP BH, ' '
				JE NEXT_CHAR_IN_STRING_WITH_RESET

				CMP BL, 13
				JE WORD_END_IN_WORD

				CMP BH, 13
				JE SENTENCE_END

				JMP NEXT_WORD_IN_STRING

			NEXT_CHAR:
				INC SI
				INC DI
				JMP WORD_LOOP

			NEXT_CHAR_IN_STRING_WITH_RESET:
				INC SI
				MOV DI, 2000H
				JMP WORD_LOOP

			NEXT_WORD_IN_STRING:
				INC SI
				MOV CL, [SI]
				CMP CL, ' '
				JE WORD_LOOP
				JMP NEXT_WORD_IN_STRING

			WORD_END_IN_WORD:
				CMP BH, ' '
				JE INCREMENT_COUNT_NEXT_WORD

				CMP BH, 13
				JE INCREMENT_COUNT_TO_END

				JMP NEXT_WORD_IN_STRING
				
			INCREMENT_COUNT_TO_END:
				INC CH
				JMP SENTENCE_END

			INCREMENT_COUNT_NEXT_WORD:
				INC CH
				INC SI
				MOV DI, 2000H

			SENTENCE_END:
				;	print("Ans: ")
				LEA DX, final
				CALL printString

				;	print count
				MOV DL, CH
				ADD DL, 48
				CALL displayChar

	STOP:
		MOV AX, 4C00H
		INT 21H

CODE ENDS
END START
