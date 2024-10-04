import socket

def client_program():
    server_host = socket.gethostname() 
    server_port = 5000  
    client_sock = socket.socket()
    client_sock.connect((server_host, server_port))  
    user_input = input(" -> ")  

    while user_input.lower().strip() != 'bye':
        client_sock.send(user_input.encode()) 
        server_response = client_sock.recv(1024).decode()  
        print('Received from server: ' + server_response)  

        user_input = input(" -> ")  
    client_sock.close() 

if __name__ == '__main__':
    client_program()
