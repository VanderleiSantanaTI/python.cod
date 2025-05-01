import socket
HOST = '' 
PORT = 5000 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    msg = con.recv(1024)
    print (msg.decode())
    msg="Ola"
    con.send(msg.encode())
    con.close()