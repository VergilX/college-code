from hamming import *
import socket

def send_message(data, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Encode the data using Hamming code
        hamming_code = calculate_parity_bits(list(map(int, data)))
        print(hamming_code)

        # Simulate an error for testing purposes (optional)
        # Uncomment to introduce an error
        # hamming_code[2] ^= 1  # Introduce a single-bit error

        # Send the Hamming code to the server
        client_socket.sendall(''.join(map(str, hamming_code)).encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")

if __name__ == "__main__":
    message = "1011"  # Sample binary input
    send_message(message)
