import socket
from crc import moduloDiv

# Driver code
MESSAGE = "1010101010"

DIVISOR = "11001"
ADDRESS = ("localhost", 9001)
SERVER = ("localhost", 9000)

DIVIDEND = MESSAGE + ("0" * (len(DIVISOR)-1))

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)

tcpsocket.connect(SERVER)

remainder = moduloDiv(DIVIDEND, DIVISOR)
print(f"Remainder: {remainder}")
print("sending:", MESSAGE+remainder)

tcpsocket.send((MESSAGE + remainder).encode(), 100)

print("Message sent successfully")

tcpsocket.close()
