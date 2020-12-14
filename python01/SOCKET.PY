import socketserver
s = socketserver.socket()          #network p2p, ipv
s.bind(("localhost",9999))
s.listen(3)
print("waiting for clint...")

while True:
    c,add = c.accept()
    print("connected with ",add)
    c.send(bytes("welcome....!"))
    c.close