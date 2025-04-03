import socket

ADDRESS = ("localhost", 9000)
SERVER_ADDRESS = ("localhost", 9001)

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)
tcpsocket.connect(SERVER_ADDRESS)

tcpsocket.send("Hello world".encode())
message = tcpsocket.recv(100)
print(f"Server message: {message.decode()}")
tcpsocket.close()
