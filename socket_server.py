import socket
import threading

clients = []

def handle_client(client_socket, client_address):
    
    message = client_socket.recv(1024).decode('utf-8') # Receive a message from Client
    if message:
        message=f'message from {message}'
    else:
        message="Enter Your message"
    broadcast(message, client_socket)
    
# Send Message to Client
def broadcast(message, client_socket):
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close() # Close the Connection
    

# Server Socket Connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address='0.0.0.0'
port=12345
try:
    server_socket.bind((ip_address, port))
except:
    print(f'Error in Binding')
server_socket.listen(1)

print(f"Server is listening on port {port}...")


# Accept the Client Connection 
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
