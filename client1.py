import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.43.1",65000))
f = open('client3.py','wb')

while True:
    datas = s.recv(1024)
    while datas:
        f.write(datas)
        datas = s.recv(1024)
    f.close()
    break
print("anji Done Recieving")
