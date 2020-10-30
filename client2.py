import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.43.41",12345))
f = open('VTS_01_3.VOB','rb')

while True:
    datas = s.recv(1024)
    while datas:
        f.write(datas)
        datas = s.recv(1024)
    f.close()
print("Done Recieving")