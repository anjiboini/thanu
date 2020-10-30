import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("enter ip address: ")
s.connect((ip,65000))
f = open(input("Enter file name with format : "),'wb')

while True:
    datas = s.recv(1024)
    while datas:
        f.write(datas)
        datas = s.recv(1024)
    f.close()
    break
 


print("anji Done Recieving")





