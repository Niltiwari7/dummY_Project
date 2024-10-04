import socket
import numpy as np

# Function to calculate modular inverse of a matrix
def mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Compute the determinant
    det_inv = pow(det, -1, mod)  # Compute the modular inverse of the determinant
    matrix_mod_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod) % mod
    return matrix_mod_inv

# Decrypt function that uses the inverse key matrix
def decrypt(cipher_text, key):
    cipher_text = [ord(c) - ord('A') for c in cipher_text]  # Convert letters to numbers (A=0, B=1, ..., Z=25)
    
    # Ensure the cipher text length is valid for the matrix size
    if len(cipher_text) % 2 != 0:
        raise ValueError("Cipher text length must be even.")

    cipher_text = np.array(cipher_text).reshape(-1, 2)  # Reshape into 2-column matrix
    key_inverse = mod_inverse(key, 26)  # Calculate modular inverse of the key matrix
    decrypted_msg = np.matmul(cipher_text, key_inverse) % 26  # Matrix multiplication and mod 26
    return ''.join([chr(int(c) + ord('A')) for c in decrypted_msg.flatten()])  # Convert numbers back to letters

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server_socket.bind(('localhost', 65432))  # Bind the socket to localhost and port 65432
    server_socket.listen(1)  # Listen for incoming connections
    print("Server is listening on port 65432...")

    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connected by {addr}")
    
    key = np.array([[2, 5], [1, 3]])  # Example 2x2 key matrix

    try:
        while True:
            cipher_text = conn.recv(1024).decode()  # Receive cipher text from client
            if not cipher_text:
                break

            print(f"Received cipher text: {cipher_text}")
            
            try:
                decrypted_text = decrypt(cipher_text, key)  # Decrypt the received cipher text
                print(f"Decrypted text: {decrypted_text}")
                conn.sendall(decrypted_text.encode())  # Send the decrypted message back to the client
            except ValueError as e:
                print(f"Decryption error: {e}")
                conn.sendall(f"Error: {e}".encode())  # Send error message if decryption fails

    except Exception as e:
        print(f"Server error: {e}")

    finally:
        conn.close()  # Close the connection when done

if __name__ == "__main__":
    start_server()
