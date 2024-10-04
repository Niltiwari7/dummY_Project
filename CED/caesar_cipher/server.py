import socket

def encrypt_message(msg, shift):
    result = ""
    for char in msg:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result

def decrypt_message(msg, shift):
    result = ""
    for char in msg:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  
    return result


def server_program():
    server_host = socket.gethostname()
    server_port = 5000  
    server_sock = socket.socket()
    server_sock.bind((server_host, server_port))
    
    server_sock.listen(2)
    conn, client_address = server_sock.accept()
    print("Connection from: " + str(client_address))
    
    shift = 3 
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        print("From connected user: " + str(data))
        
        encrypted_data = encrypt_message(data, shift)
        print("Encrypted data: " + encrypted_data)
        
        decrypted_data = decrypt_message(encrypted_data, shift)
        print("Decrypted data: " + decrypted_data)
        
        conn.send(encrypted_data.encode())  
    
    conn.close()


if __name__ == '__main__':
    server_program()
