import binascii
import socket

def calculate_crc(data):
    """Calculate the CRC32 of the given data."""
    return binascii.crc32(data) & 0xffffffff  # Ensure it's unsigned


def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                message, received_crc = data[:-4], int.from_bytes(data[-4:], byteorder='big')
                calculated_crc = calculate_crc(message)

                print(f"Received message: {message.decode('utf-8')}")
                print(f"Received CRC: {received_crc}, Calculated CRC: {calculated_crc}")

                if received_crc == calculated_crc:
                    response = "CRC Check Passed"
                else:
                    response = "CRC Check Failed"
                
                conn.sendall(response.encode('utf-8'))


start_server()
