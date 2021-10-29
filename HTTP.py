#Cmpt 325 Group-6
#HW-3

## imports socket and system to terminate the program
from socket import *
import sys

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

#Preparing server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Port number used
serverPort=1435

#Binding the server socket by fetching the IP address and using the ports.
serverSocket.bind((ip_address, serverPort))
serverSocket.listen(5)


while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print ('Got connection from', addr)
    
    try:
        #Name of the file in the directory to be accessed.
        filename = "index"
       
        #opening and reading from the file
        f = open(filename+".html")
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        print(outputdata)
        link = '\nHTTP/1.1 200 OK\n\n'
        connectionSocket.send(link.encode())
        connectionSocket.send(outputdata.encode())
        
    #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
    except IOError:
    #Exception when file cannot be found
    #Send response message for file not found
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())

#Close client socket

connectionSocket.close()
serverSocket.close()

#Terminate the program after sending the corresponding data
sys.exit()
