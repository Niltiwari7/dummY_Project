import socket

def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]

def locindex(c, my_matrix):
    loc = []
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
    return loc

def encrypt(msg, my_matrix):
    msg = msg.upper().replace(" ", "")
    i = 0
    # Handle repeated letters by adding 'X'
    while i < len(msg):
        if i < len(msg) - 1 and msg[i] == msg[i + 1]:
            msg = msg[:i + 1] + 'X' + msg[i + 1:]
        i += 2
    # Add 'X' if the message length is odd
    if len(msg) % 2 != 0:
        msg += 'X'
    
    cipher_text = []
    i = 0
    while i < len(msg):
        loc = locindex(msg[i], my_matrix)
        loc1 = locindex(msg[i + 1], my_matrix)
        
        if loc[1] == loc1[1]:  # Same column
            cipher_text.append(my_matrix[(loc[0] + 1) % 5][loc[1]])
            cipher_text.append(my_matrix[(loc1[0] + 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:  # Same row
            cipher_text.append(my_matrix[loc[0]][(loc[1] + 1) % 5])
            cipher_text.append(my_matrix[loc1[0]][(loc1[1] + 1) % 5])
        else:  # Rectangle swap
            cipher_text.append(my_matrix[loc[0]][loc1[1]])
            cipher_text.append(my_matrix[loc1[0]][loc[1]])
        
        i += 2
    return ''.join(cipher_text)

def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    result = []

    # Generate key matrix
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

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))  # Connect to server on port 65432
    
    try:
        key = "SECURITY"
        my_matrix = generate_key_matrix(key)

        msg = input("Enter message: ")
        cipher_text = encrypt(msg, my_matrix)
        print(f"Cipher text: {cipher_text}")
        
        # Send the cipher text to the server
        client_socket.sendall(cipher_text.encode())

        # Receive the server response
        decrypted_text = client_socket.recv(1024).decode()
        print(f"Decrypted text from server: {decrypted_text}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()  # Close the connection when done

if __name__ == "__main__":
    start_client()
