import socket

"""
Step 1: Decide the base and the modulus
Step 2: Keep a private key
Step 3: Share the base and modulus with other end point
Step 4: Calculate public_key = (base)^(private_key) % (modulus)
Step 5: Exchange public keys
Step 6: Find secret_key = (other_pub_key)^(private_key) % (modulus)

"""

# Pre-defined values
BASE = 3
MOD = 19
INT_SIZE = 4

PRIVATE_KEY = 7

ADDRESS = ("localhost", 9001)
SERVER = ("localhost", 9000)

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)
tcpsocket.connect(SERVER)

# Assume client shares BASE and MOD already
public_key = str((BASE ** PRIVATE_KEY) % MOD)

# Share public key
tcpsocket.send(public_key.encode(), INT_SIZE)

# Receive server public key 
recv_key = int(tcpsocket.recv(INT_SIZE).decode())

# Find secret key and print
secret_key = (recv_key ** PRIVATE_KEY) % MOD

print("Calculated secret key:", secret_key)

tcpsocket.close()
