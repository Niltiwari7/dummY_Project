import socket

# Diffie-Hellman Key Exchange
P = int(input('Please enter the value of P: '))
g = int(input('Please enter the value of g: '))
a = int(input("Please enter the value of a: "))

# Compute A = g^a mod P
A = (g ** a) % P
print(f"\nClient (A1) sends A = {A}")

# Function to extend the key based on the length of the message
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# XOR-based encryption function
def encrypt(message, key):
    # Simple XOR encryption (for demonstration)
    return ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(message, key)])

# Client-side socket to communicate with the server
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))  # Connect to the server

    # Send client's public value A to the server
    client_socket.sendall(str(A).encode())

    # Receive server's public value B
    B = int(client_socket.recv(1024).decode())
    print(f"Server (B2) sends B = {B}")

    # Calculate the shared secret using Diffie-Hellman
    shared_secret = (B ** a) % P
    print(f"\nClient Shared Secret: {shared_secret}")

    # Message to be encrypted
    msg = "Hello server"

    # Generate key using shared secret
    key = generateKey(msg, str(shared_secret))

    # Encrypt the message
    cipher_text = encrypt(msg, key)
    print(f"Cipher Text: {cipher_text}")

    # Send the encrypted message to the server
    client_socket.sendall(cipher_text.encode())

    # Receive and decrypt the response from the server
    decrypted_text = client_socket.recv(1024).decode()
    print(f"Decrypted Successfully from the server: {decrypted_text}")

    # Close the client socket
    client_socket.close()

# Ensure the client script starts
if __name__ == "__main__":
    start_client()
