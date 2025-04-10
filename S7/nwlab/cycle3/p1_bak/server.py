# Returns XOR of 'a' and 'b' 
# (both of same length) 


def xor(a, b): 

	# initialize result 
	result = [] 

	# Traverse all bits, if bits are 
	# same, then XOR is 0, else 1 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 


# Performs Modulo-2 division 
def mod2div(dividend, divisor): 

	# Number of bits to be XORed at a time. 
	pick = len(divisor) 

	# Slicing the dividend to appropriate 
	# length for particular step 
	tmp = dividend[0: pick] 

	while pick < len(dividend): 

		if tmp[0] == '1': 

			# replace the dividend by the result 
			# of XOR and pull 1 bit down 
			tmp = xor(divisor, tmp) + dividend[pick] 

		else: # If leftmost bit is '0' 
			# If the leftmost bit of the dividend (or the 
			# part used in each step) is 0, the step cannot 
			# use the regular divisor; we need to use an 
			# all-0s divisor. 
			tmp = xor('0'*pick, tmp) + dividend[pick] 

		# increment pick to move further 
		pick += 1

	# For the last n bits, we have to carry it out 
	# normally as increased value of pick will cause 
	# Index Out of Bounds. 
	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 

# Function used at the sender side to encode 
# data by appending remainder of modular division 
# at the end of data. 


def encodeData(data, key): 

	l_key = len(key) 

	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	# Append remainder in the original data 
	codeword = data + remainder 


# Driver code 
data = "100100"
key = "1101"
encodeData(data, key) 


# Perform with sockets
host = "localhost"
port = 1080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('', port))
print(f"Binded to port: {port}")

# host_ip = socket.gethostbyname('localhost')
sock.listen(5)  # 5 queue

while True:
    c, addr = sock.accept()
    print("Got connection from", addr)

    c.send("Thank you for connecting".encode())
    data = c.recv(1024).decode()
    print("Performing CRC check...")

    remainder = encodeData(data, 

    print(f"Received data from client: {data}")

    c.close()

    break
