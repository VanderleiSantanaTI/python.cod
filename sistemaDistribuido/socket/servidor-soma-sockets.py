import socket
HOST = '' 
PORT = 5123 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    msg = con.recv(1024)
    print (msg.decode())
    m = msg.decode()
    a , b = m.split(';')
    na=int(a)
    nb=int(b)
    nr=na+nb
    r=str(nr)
    con.send(r.encode())
    con.close()