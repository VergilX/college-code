import socket

host = "localhost"
port = 1080
message = "Hello there"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

sock.send(message.encode())

print(sock.recv(1024).decode())

sock.close()
