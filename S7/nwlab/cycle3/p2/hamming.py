def calculate_parity_bits(data_bits):
    """Calculate parity bits for Hamming code."""
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    # Create an array for the codeword
    codeword = [0] * (m + r)

    # Insert data bits into the codeword array
    j = 0
    for i in range(1, len(codeword) + 1):
        if (i & (i - 1)) != 0:  # If not a power of 2
            codeword[i - 1] = data_bits[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_index = 2 ** i
        parity_value = 0
        for j in range(1, len(codeword) + 1):
            if j & parity_index:  # Check if the j-th bit is included
                parity_value ^= codeword[j - 1]
        codeword[parity_index - 1] = parity_value

    return codeword

def decode_hamming(codeword):
    """Decode Hamming code and correct single-bit errors."""
    m = len(codeword)
    r = 0
    while (2 ** r) < (m + 1):
        r += 1

    # Calculate the parity bits
    error_position = 0
    for i in range(r):
        parity_index = 2 ** i
        parity_value = 0
        for j in range(1, len(codeword) + 1):
            if j & parity_index:  # Check if the j-th bit is included
                parity_value ^= codeword[j - 1]
        if parity_value != 0:
            error_position += parity_index

    # Correct the error if one exists
    if error_position != 0:
        codeword[error_position - 1] ^= 1  # Flip the erroneous bit

    # Extract the original data bits
    data_bits = []
    for i in range(1, len(codeword) + 1):
        if (i & (i - 1)) != 0:  # If not a power of 2
            data_bits.append(codeword[i - 1])

    return data_bits, error_position
