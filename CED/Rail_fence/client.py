import socket

def client_program():
    server_host = socket.gethostname() 
    server_port = 5000  
    client_sock = socket.socket() 

    client_sock.connect((server_host, server_port))

    plaintext = input("Enter the plaintext: ")
    num_rails = input("Enter the number of rails: ")
    
    while plaintext.lower().strip() != 'bye':
        client_sock.send(f"{plaintext}|{num_rails}".encode())

        server_response = client_sock.recv(1024).decode()
        print('Received from server: ' + server_response)

        plaintext = input("Enter the plaintext: ")
        num_rails = input("Enter the number of rails: ")
    client_sock.close()

if __name__ == '__main__':
    client_program()
