import binascii
import socket

def calculate_crc(data):
    """Calculate the CRC32 of the given data."""
    return binascii.crc32(data) & 0xffffffff  # Ensure it's unsigned

def send_message(message, crc=None, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        # Calculate the CRC for the message
        if not crc:
            crc = calculate_crc(message.encode('utf-8'))
        data_to_send = message.encode('utf-8') + crc.to_bytes(4, byteorder='big')
        
        client_socket.sendall(data_to_send)
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")

message = "100100"
send_message(message)
