import socket

def xor(m, k):
    result = []
    for i, j in zip(m, k):
        result.append(chr(ord(i) ^ ord(j)))  
    return "".join(result)

def encrypt(plain_text, key):
    return xor(plain_text, key)

def decrypt(cipher_text, key):
    return xor(cipher_text, key)

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    print("Server is listening...")
    
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    
    key = 'crypt'
    

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        print("From connected user: " + str(data))
        
        encrypted_data = encrypt(data, key)
        print("Encrypted data: " + encrypted_data)
        
        decrypted_data = decrypt(encrypted_data, key)
        print("Decrypted data: " + decrypted_data)
        
        conn.send(encrypted_data.encode())
    
    conn.close()

if __name__ == '__main__':
    server_program()
