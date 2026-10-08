import socket

client = socket.socket()
client.connect(('localhost', 5000))

msg = input("Enter message to send: ")
client.sendall(msg.encode())

response = client.recv(1024).decode()
print("Server Echoed:", response)

client.close()