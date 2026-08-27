import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 235))

# Send message to server
client_socket.send("Hello from Client!".encode())

# Receive response from server
data = client_socket.recv(1023).decode()
print("Server says:", data)

# Closing connection
client_socket.close()
