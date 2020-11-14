from socket import *


serversocket = socket(AF_INET, SOCK_STREAM)

serversocket.bind(('', 65432))
serversocket.listen()

while True :
    clientsocket, address = serversocket.accept()
    clientsocket.send(('HTTP/1.1 200 OK\n' + 'Content-Type: text/html\n' + '\n' + '<html><body>Hello World! </body></html>').encode())
    clientsocket.shutdown(SHUT_WR)
    clientsocket.close()
serversocket.close()
