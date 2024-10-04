import socket

def client_program():
    server_host = socket.gethostname()
    server_port = 5000 
    client_sock = socket.socket()
    
    client_sock.connect((server_host, server_port))
    
    user_message = input("Enter the message: ")
    encryption_key = input("Enter the key: ")
    
    while user_message.lower().strip() != 'bye':
        client_sock.send(f"{user_message}|{encryption_key}".encode())
        
        server_response = client_sock.recv(1024).decode()
        print('Received from server: ' + server_response)
        
        user_message = input("Enter the message: ")
        encryption_key = input("Enter the key: ")
    
    client_sock.close()

if __name__ == '__main__':
    client_program()
