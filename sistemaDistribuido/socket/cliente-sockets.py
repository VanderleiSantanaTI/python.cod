import socket
HOST = '<IP>'
PORT = 5000 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = "Ola Mundo"
tcp.send(msg.encode())
msg=tcp.recv(1024)
print(msg.decode())
tcp
tcp.close()