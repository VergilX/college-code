import socket

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
    print(f"Received data from client: {data}")

    c.close()

    break
