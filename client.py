#imports
#Sys to read command line arguments
from socket import *
import sys

#The commandline arguments would be formatted as:
#client.py server_host server_port filename


#Host server name and port number
serverName = sys.argv[1]
serverPort = sys.argv[2]
filename = sys.argv[3]+".html"

#Preparing client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Connecting to the server and sending a GET request to obtain data.
clientSocket.connect((serverName, serverPort))
outputdata = f'GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\n\r\n'
clientSocket.send(outputdata.encode())

#While data is true, print the information recieved 
data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end = '')

#Close socket after information is printed
clientSocket.close()
