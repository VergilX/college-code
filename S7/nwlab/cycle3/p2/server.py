from hamming import *
import socket

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
                
                # Convert received bytes to a list of integers
                received_bits = list(map(int, data.decode('utf-8')))
                print(f"Received Hamming code: {received_bits}")

                # Decode and correct the data
                corrected_data, error_position = decode_hamming(received_bits)
                response = f"Corrected data: {corrected_data}, Error position: {error_position if error_position else 'No error'}"
                conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
