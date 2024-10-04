import socket


def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return "".join(key)
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_encrypt(msg, key):
    key = generate_key(msg, key)
    cipher_text = []
    for i in range(len(msg)):
        if msg[i].isalpha():
            shift = (ord(msg[i].upper()) + ord(key[i].upper())) % 26
            cipher_text.append(chr(shift + ord('A')))
        else:
            cipher_text.append(msg[i])
    return "".join(cipher_text)


def vigenere_decrypt(cipher_text, key):
    key = generate_key(cipher_text, key)
    original_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(cipher_text[i]) - ord(key[i].upper()) + 26) % 26
            original_text.append(chr(shift + ord('A')))
        else:
            original_text.append(cipher_text[i])  
    return "".join(original_text)


def server_program():
    server_host = socket.gethostname()
    server_port = 5000
    server_sock = socket.socket()
    server_sock.bind((server_host, server_port))
    
    server_sock.listen(2)
    print("Server is listening...")
    
    while True:
        conn, client_address = server_sock.accept()
        print("Connection from: " + str(client_address))
        
        data = conn.recv(1024).decode()
        if not data:
            break
        
        msg, key = data.split('|')
        encrypted_msg = vigenere_encrypt(msg, key)
        decrypted_msg = vigenere_decrypt(encrypted_msg, key)
        
        response = f"Encrypted message: {encrypted_msg}\nDecrypted message: {decrypted_msg}"
        conn.send(response.encode())
        
        conn.close()

if __name__ == '__main__':
    server_program()
