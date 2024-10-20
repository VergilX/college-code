import socket
import sys

port = 1080

if len(sys.argv) != 2:
    print("Usage: python3 tcp_file_client.py <filename>")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('', port))

with open(sys.argv[1], 'r') as f:
    content = f.read(1024)

    sock.send(content.encode())

print("Content sent successfully")
