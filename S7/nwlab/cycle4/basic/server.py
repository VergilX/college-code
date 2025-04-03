import socket

ADDRESS = ("localhost", 9001)

tcpsocket = socket.socket()
tcpsocket.bind(ADDRESS)

tcpsocket.listen(5)
print("Server listening at port 8090")

while True:
    conn, addr = tcpsocket.accept()
    message = conn.recv(10).decode()

    # Step 1: Ask which cipher will be used
    conn.send("")

    print(f"Message received from client {addr}: {message}")
    conn.send(f"{message}".encode())

tcpsocket.close()
