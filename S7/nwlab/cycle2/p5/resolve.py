import subprocess
import socket

RESOLVE = dict()

with open('hosts', 'r') as f:
    for line in f:
        ip, host = line.split()
        RESOLVE[ip] = host

print(RESOLVE)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode()
    if data in RESOLVE:
        print(f"Resolved address for {data}:", RESOLVE[data])
    else:
        print("Hostname not present in hosts file")
