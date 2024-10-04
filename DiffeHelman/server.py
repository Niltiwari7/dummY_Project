import socket

# Server-side Diffie-Hellman setup
P = int(input('Please enter the value of P: '))
g = int(input('Please enter the value of g: '))
b = int(input("\nPlease enter the value of b: "))

# Server generates its public value B
B = (g ** b) % P
print("Server (B2) will send B =", B)

# Function to extend the key based on the length of the text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# XOR-based decryption
def decrypt(cipher_text, key):
    return ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(cipher_text, key)])

# XOR-based encryption (same as decryption because XOR is symmetric)
def encrypt(plain_text, key):
    return ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(plain_text, key)])

# Server socket to handle client connections
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("Server is waiting for a connection ... ")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive the client's public value A
    A = int(conn.recv(1024).decode())
    print(f"Client (A1) sends A = {A}")

    # Send the server's public value B to the client
    conn.sendall(str(B).encode())

    # Calculate the shared secret using Diffie-Hellman
    shared_secret = (A ** b) % P
    print(f"\nServer Shared Secret: {shared_secret}")

    # Receive the encrypted message from the client
    cipher_text = conn.recv(1024).decode()
    print(f"Received Cipher Text: {cipher_text}")

    # Generate the key using the shared secret
    key = generateKey(cipher_text, str(shared_secret))

    # Decrypt the message
    decrypted_text = decrypt(cipher_text, key)
    print(f"Decrypted Message: {decrypted_text}")

    # Prepare a response message
    response_message = "Hello, Client!"
    response_key = generateKey(response_message, str(shared_secret))

    # Encrypt the response message
    response_cipher_text = encrypt(response_message, response_key)

    # Send the encrypted response back to the client
    conn.sendall(response_cipher_text.encode())

    # Close the connection
    conn.close()

# Start the server when the script is executed
if __name__ == "__main__":
    start_server()
