; Program to add 2 8-bit decimal digits

DATA SEGMENT
    INP1 DB "Enter first number: $"
    INP2 DB "Enter second number: $"
    OUTPUT DB "Sum: $"
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
    START:
        ; Set DS segment register
        MOV AX, DATA
        MOV DS, AX

        ; First input
        LEA DX, INP1
        MOV AH, 09H
        INT 21H
        CALL GETNUM
        MOV CX, AX ; Store the result from procedure in CX

        ; Second input
        MOV AH, 09H
        LEA DX, INP2
        INT 21H
        CALL GETNUM ; Keep the result from proc in AX

        ; Actually you don't even need the AX full registers since it will be
        ; limited to 8-bit numbers due to addition
        ; But since input requires MUL, we are forced to use the AX register

        ; Add the numbers ( CX+AX )
        ADD CX, AX
        MOV BX, CX ; Store result in BX as DISPLAY uses BX

        ; Printing output
        CALL DISPLAY

        STOP:
            MOV AH, 4CH
            INT 21H

        ; Procedure to display 16-bit hex
        DISPLAY PROC
            ; Display message
            MOV AH, 09H
            LEA DX, OUTPUT
            INT 21H

            ; BH will contain the carry so convert that first
            ADD BH, 30H
            MOV AH, 02H
            MOV DL, BH
            INT 21H
            
            ; Put the tens place into BH
            MOV DL, 10H
            MOV BH, 00H ; Clearing higher bit
            MOV AX, BX
            DIV DL
            MOV BH, AL
            MOV BL, AH ; Remainder in ones place
                       
            ; Convert to ASCII and display
            ADD BH, 30H
            ADD BL, 30H
            
            ; Display
            MOV DL, BH
            MOV AH, 02H
            INT 21H
            
            MOV DL, BL
            MOV AH, 02H
            INT 21H
            RET
        DISPLAY ENDP

        ; Procedure to get 8-bit hex in AX
        GETNUM PROC
            MOV AH, 01H
            INT 21H

            SUB AL, 30H ; Convert to HEX ( it's a fact :] )

            ; Multiply with 10H to get to second digit
            MOV DL, 10H
            MUL DL ; Stores result in AX
            MOV BX, AX

            ; Second digit
            MOV AH, 01H
            INT 21H

            SUB AL, 30H ; Converting to HEX
            MOV AH, 00H ; Clearing higher nibble of AX

            ADD AX, BX
            RET
        GETNUM ENDP
CODE ENDS
END START
