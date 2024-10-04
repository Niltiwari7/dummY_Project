import socket

def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]

def locindex(c, my_matrix): 
    # Get the location of each character
    loc = []
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
    return loc

def decrypt(msg, my_matrix):
    msg = msg.upper().replace(" ", "")
    plain_text = []
    i = 0
    while i < len(msg):
        loc = locindex(msg[i], my_matrix)
        loc1 = locindex(msg[i + 1], my_matrix)
        
        if loc[1] == loc1[1]:  # Same column
            plain_text.append(my_matrix[(loc[0] - 1) % 5][loc[1]])
            plain_text.append(my_matrix[(loc1[0] - 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:  # Same row
            plain_text.append(my_matrix[loc[0]][(loc[1] - 1) % 5])
            plain_text.append(my_matrix[loc1[0]][(loc1[1] - 1) % 5])
        else:  # Rectangle swap
            plain_text.append(my_matrix[loc[0]][loc1[1]])
            plain_text.append(my_matrix[loc1[0]][loc[1]])
        
        i += 2
    return ''.join(plain_text)

def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    result = []
    
    # Create key matrix
    for c in key:
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)
    
    for i in range(65, 91):  # A-Z ASCII
        if chr(i) not in result:
            if i == 73 and 'J' not in result:
                result.append("I")
            elif i == 74 and 'I' in result:
                continue
            else:
                result.append(chr(i))

    k = 0
    my_matrix = matrix(5, 5, 0)
    
    for i in range(5):
        for j in range(5):
            my_matrix[i][j] = result[k]
            k += 1

    return my_matrix

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening on port 65432...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    try:
        key = "MONARCHY"
        my_matrix = generate_key_matrix(key)

        while True:
            cipher_text = conn.recv(1024).decode()
            if not cipher_text:
                break
            print(f"Received cipher text: {cipher_text}")

            decrypted_text = decrypt(cipher_text, my_matrix)
            print(f"Decrypted text: {decrypted_text}")
            
            conn.sendall(decrypted_text.encode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    start_server()
