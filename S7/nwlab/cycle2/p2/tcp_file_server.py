import socket
import sys

port = 1080

if len(sys.argv) != 2:
    print("Usage: python3 tcp_file_server.py <filename>")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))

sock.listen(5)


f = open(sys.argv[1], 'w')
while True:
    c, addr = sock.accept()

    data = c.recv(1024).decode()
    if data:
        f.write(data)

    while data:
        data = c.recv(1024).decode()
        f.write(data)


    c.close()
    print(f"Data transfer complete! Stored in {sys.argv[1]}")
    break

f.close()


# reading file contents
with open(sys.argv[1], 'r') as f:
    for line in f:
        print(line)
