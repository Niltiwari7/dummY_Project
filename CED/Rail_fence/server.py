import socket

def rail_fence_encrypt(message, rails):
    fence = [['' for _ in range(len(message))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for char in message:
        fence[row][col] = char
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction
        col += 1

    ciphertext = ''.join([''.join(row) for row in fence])
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0 or row == rails - 1:
            direction *= -1
        fence[row][col] = '*'
        row += direction
        col += 1

    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1

    message = []
    row, col = 0, 0
    direction = -1

    for i in range(len(ciphertext)):
        message.append(fence[row][col])
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction
        col += 1

    return ''.join(message)

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
        message, rails = data.split('|')  
        rails = int(rails) 
        encrypted_msg = rail_fence_encrypt(message, rails) 
        decrypted_msg = rail_fence_decrypt(encrypted_msg, rails) 
        response = f"Encrypted message: {encrypted_msg}\nDecrypted message: {decrypted_msg}" 
        conn.send(response.encode())  
        conn.close()  

if __name__ == '__main__':
    server_program()
