from crc import moduloDiv
import socket

ADDRESS = ("localhost", 9000)

DIVISOR = "11001"

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)

tcpsocket.listen(5)
print("Listening at port 9000")

conn, addr = tcpsocket.accept()

message = conn.recv(100).decode()
print(f"Received message: {message}")

remainder = moduloDiv(message, DIVISOR)

for i in range(len(remainder)):
    if remainder[i] != "0":
        print("Error in received bit stream. Abort")
        exit(1)

print("No error in received bit stream")
