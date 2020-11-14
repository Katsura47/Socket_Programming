import socket

serverPORT = 65432
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(('', serverPORT))
print('Server is ready to service')

while True:
    try:
        message, clientAddress = serverSocket.recvfrom(2048)
        bc = message.decode().split(' ')
        c = int(bc[0]) + int(bc[1])
        b = int(bc[1])
        newmess = str(b) + ' ' + str(c)
        serverSocket.sendto(newmess.encode(), clientAddress)
        print(clientAddress)

    except:
        print('Unexcepted Error!')
        break


    