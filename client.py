#imports
from socket import *

#Host server name and port number
serverName = '10.30.86.26'
serverPort = 1435

#Preparing client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connecting to the server and sending a GET request to obtain data.
clientSocket.connect((serverName, serverPort))
outputdata = 'GET /index.html HTTP/1.1\r\nHost: 10.30.86.26\r\n\r\n'
clientSocket.send(outputdata.encode())

#While data is true, print the information recieved 
data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end = '')

#Close socket after information is printed
clientSocket.close()
