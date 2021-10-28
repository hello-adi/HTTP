from socket import *

serverName = '10.6.70.200'
serverPort = 1435
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
outputdata = 'GET /index.html HTTP/1.1\r\nHost: 10.6.70.200\r\n\r\n'
clientSocket.send(outputdata.encode())
data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end = '')
clientSocket.close()
