import socket
import time
servername = '127.0.0.1'
serverPORT = 65432

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a = 10
b = 1
c = 1
while True:
    print(b, c)
    message = str(b) + ' ' + str(c)
    clientSocket.sendto(message.encode(), (servername, serverPORT))
    newfib, serverAddress = clientSocket.recvfrom(2048)
    bc = newfib.decode().split(' ')
    c = int(bc[1])
    b = int(bc[0])
    

    time.sleep(1)
    a -= 1
    if a == 0:
        break


clientSocket.close()