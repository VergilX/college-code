"""
This server checks if the given 7-bit Hamming code is right
or not. Returns error bit

FOLLOWING EVEN PARITY BY DEFAULT

Rules:
    - The Hamming bit should be 7 6 5 4 3 2 1
    - Parity: 1, 2, 4
    - P1 -> D3, D5, D7
    - P2 -> D3, D6, D7
    - P3 -> D5, D6, D7

Correction:
    - If odd, set parity to 1
    - Put parity bits together to find the error bit
"""

def verifyHammingCode(code: str, evenParity=True):
    """
        Verifies Hamming Code and finds error if any
        parity = True : Even parity
                 False: Odd parity

        Returns -1 if no error
        Else returns index in 7 6 5 4 3 2 1
    """

    if len(code) != 7:
        print("Invalid size. Has to be 7 bits")
        exit(1)


    # Reverse code
    code = code[-1::-1]

    p1 = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6])
    p2 = int(code[1]) + int(code[2]) + int(code[5]) + int(code[6])
    p3 = int(code[3]) + int(code[4]) + int(code[5]) + int(code[6])

    error_present = False
    if evenParity:
        if p1 % 2 != 0:
            error_present = True
            p1 = 1
        else:
            p1 = 0

        if p2 % 2 != 0:
            error_present = True
            p2 = 1
        else:
            p2 = 0

        if p3 % 2 != 0:
            error_present = True
            p3 = 1
        else:
            p3 = 0

    else:
        if p1 % 2 == 0:
            error_present = True
            p1 = 1
        else:
            p1 = 0

        if p2 % 2 == 0:
            error_present = True
            p2 = 1
        else:
            p2 = 0

        if p3 % 2 == 0:
            error_present = True
            p3 = 1
        else:
            p3 = 0

    if not error_present:
        print("No error in Hamming Code")
        return -1

    # Get binary
    position = p3*4 + p2*2 + p1
    print(code)

    print("Error at position", position)
    return int(position)

print(verifyHammingCode("1111101"))
