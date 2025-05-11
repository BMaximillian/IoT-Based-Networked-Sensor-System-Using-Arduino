import socket
import time

# Server settings
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server listening on port", PORT)

# Log file
log_file = open("temperature_log.txt", "a")

while True:
    # Accept client connection
    client_socket, addr = server_socket.accept()
    print("Connected to:", addr)

    # Receive data
    data = client_socket.recv(1024).decode()
    if data:
        temp = float(data)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: Temperature = {temp} C\n"
        print(log_entry.strip())
        log_file.write(log_entry)
        log_file.flush()

    client_socket.close()