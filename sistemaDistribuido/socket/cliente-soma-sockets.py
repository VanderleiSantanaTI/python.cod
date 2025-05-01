import socket
HOST = '<IP>'
PORT = 5123 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
a = input('entre com o valor de a:')
b = input('entre com o valor de b:')
tcp.send(a.encode()+";".encode()+b.encode())
r=tcp.recv(1024)
print(r.decode())
tcp.close()

