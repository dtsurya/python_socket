import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
ip_address="Enter IP Address"
port= "Enter Port"
client_socket.connect((ip_address, port))

message="Enter Message here.."   # Send to Server
client_socket.sendall(message.encode('utf-8'))

# Receive a message from the server
message = client_socket.recv(1024)
print(message.decode('utf-8'))

# Close the socket
client_socket.close()
