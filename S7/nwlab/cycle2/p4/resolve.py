import subprocess
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    stdout = subprocess.run(['nslookup', data], capture_output=True)
    print(f"Resolved address for {data}: ")
    print(stdout.stdout.decode())  # or don't use capture_output
