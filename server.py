import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost on port 235
server_socket.bind(('localhost', 235))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 235...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from client
data = conn.recv(1023).decode()
print("Client says:", data)

# Send response back to client
conn.send("Hello from Server!".encode())

# Closing connection
conn.close()
server_socket.close()
