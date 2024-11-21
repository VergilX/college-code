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

PRIVATE_KEY = 10

ADDRESS = ("localhost", 9000)

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)
tcpsocket.listen(5)

conn, addr = tcpsocket.accept()

# Assume client shares BASE and MOD already
public_key = str((BASE ** PRIVATE_KEY) % MOD)

# Receive client public key 
recv_key = int(conn.recv(INT_SIZE).decode())

# Share public key
conn.send(public_key.encode(), INT_SIZE)

# Find secret key and print
secret_key = (recv_key ** PRIVATE_KEY) % MOD

print("Calculated secret key:", secret_key)

conn.close()
tcpsocket.close()
