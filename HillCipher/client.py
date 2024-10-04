import socket
import numpy as np

# Function to encrypt the message using a key matrix
def encrypt(msg, key):
    msg = msg.upper().replace(' ', '')  # Convert message to uppercase and remove spaces
    
    # Ensure the message length is even by appending 'X' if necessary
    if len(msg) % 2 == 1:
        msg += 'X'

    # Convert message letters to numbers (A=0, B=1, ..., Z=25)
    msg = [ord(c) - ord('A') for c in msg]
    msg = np.array(msg).reshape(-1, 2)  # Reshape message into 2-column matrix

    key = np.array(key).reshape(2, 2)  # Ensure key is a 2x2 matrix
    encrypted_msg = np.matmul(msg, key) % 26  # Encrypt using matrix multiplication and mod 26

    # Convert encrypted numbers back to letters
    return ''.join([chr(c + ord('A')) for c in encrypted_msg.flatten()])

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    client_socket.connect(('localhost', 65432))  # Connect to the server

    key = np.array([[2, 5], [1, 3]])  # Example key matrix
    msg = input("Please enter the message: ")  # Take input from the user

    cipher_text = encrypt(msg, key)  # Encrypt the message
    print(f"Cipher Text: {cipher_text}")

    client_socket.sendall(cipher_text.encode())  # Send the encrypted message to the server

    decrypted_text = client_socket.recv(1024).decode()  # Receive decrypted text from server
    print(f"Decrypted Successfully from the server: {decrypted_text}")

    client_socket.close()  # Close the connection

if __name__ == "__main__":
    start_client()
