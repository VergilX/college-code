"""
Step 1: Determine divisor and message
Step 2: Append k-1 0's to dividend
Step 3: Perform modulo division with new dividend
    3.1 Determine length of divisor n
    3.2 Take n bits from dividend
    3.3 Perform xor
    3.4 Determine number of leading 0s (s)
    3.5 Add n-s to current dividend
    3.6 Repeat from 3.3 until dividend is finished
Step 4: Append remainder to original message
Step 5: Send to endpoint
"""

def xor(a: str, b: str):
    n = len(a)
    if n != len(b):
        print("Args should be of same length")
        exit(1)

    ans = ""
    for i in range(n):
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"

    return ans


def moduloDiv(dividend: str, divisor: str):
    # Returns remainder
    div_len = len(divisor)
    start = 0
    n = len(dividend)
    end = div_len
    temp = dividend[start:end]

    while end <= n:
        print(temp, divisor)
        if temp[0] == "1":
            result = xor(temp, divisor)
        else:
            result = xor(temp, "0"*(end-start))
        print(result)

        # Calculate leading 0s
        zero_count = 0
        for i in range(div_len):
            if result[i] == "0":
                zero_count += 1
            else:
                break

        start = end
        end += zero_count
        print(f"start: {start}, end: {end}, zeros: {zero_count}")
        temp = result[zero_count:] + dividend[start:end]



    # Extract last (div_len-1) bits
    return (result + dividend[start:])[-(div_len-1):]
