from socket import *
from encode import encode_
import time


mailserver = ("smtp.gmail.com", 587)

clientSocket = socket(AF_INET, SOCK_STREAM)



def send_msg(clientSocket, msg, printing=True, encoding=True):
    if encoding:
        clientSocket.send(msg.encode())
    else:
        clientSocket.send(msg)
    if printing:
        recv = clientSocket.recv(2048)
        print('Received Message is: ', recv.decode())



def auth_and_init(username, passw):
    helocom = 'helo google\r\n'
    send_msg(clientSocket, helocom)
    auth1 = 'starttls auth login\r\n'
    send_msg(clientSocket, auth1)
    auth2 = 'auth login\r\n'
    send_msg(clientSocket, auth2)
    send_msg(clientSocket, encode_(username), False, False)
    send_msg(clientSocket, '\r\n', False)
    print('Username Given')
    send_msg(clientSocket, encode_(passw), False, False)
    send_msg(clientSocket, '\r\n',False)
    print('Password Given')


clientSocket.connect(mailserver)
recv = clientSocket.recv(2048)
recv = recv.decode()
print('Message After Connection Request', recv)

if recv[:3] != '220':
    print('220 reply not received from server')






username = 'yusufakdo.47@gmail.com'
passw = ''

auth_and_init(username, passw)




print('First Phase')

mailto = 'MAIL FROM:<inzva>\r\n'
rcptto = 'RCPT TO:<ak.akdogan47@gmail.com>\r\n'



send_msg(clientSocket, mailto)
send_msg(clientSocket, rcptto)


data = '\r\n Hello, Dear Yusuf I am sending this mail from code so appreciate it please.'


send_msg(clientSocket, 'DATA\r\n')


subj = 'Subject: My Subj\r\n\r\n'
send_msg(clientSocket, subj)
print(subj)
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + '\r\n\r\n'
send_msg(clientSocket, date)
print('date')
send_msg(clientSocket, data, False)
print('msg')
send_msg(clientSocket, '\r\n.\r\n')
send_msg(clientSocket, 'QUIT\r\n')


clientSocket.close()
