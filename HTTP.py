## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort=6969

serverSocket.bind(('127.0.0.1', serverPort))#you can change the ip
serverSocket.listen(5)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message = "index"#Fill in start #Fill in end
        #filename = message.split()[1]
        f = open(filename+".html")
        outputdata = f.read()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        print (outputdata) 
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
        connectionSocket.send(outputdata)
        #Fill in end
#Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:



#Send response message for file not found
#Fill in start
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
#Fill in end
#Close client socket
#Fill in start
connectionSocket.close()
#Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data