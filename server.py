#import socket module
from socket import *
import sys # In order to terminate the program
def webServer(port=6789):
    serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a server socket
    #Fill in start
    #HOST = '192.168.31.230'
    serverSocket.bind(("",port))
    serverSocket.listen()
    #Fill in end
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  #Fill in start #Fill in end
        try:
            message = connectionSocket.recv(1024)#Fill in start #Fill in end
            print("Message: ",message)
            filename = message.split()[1]
            print(filename)
            f = open(filename[1:])
            outputdata = f.read()#Fill in start #Fill in end
            #Send one HTTP header line into socket
            header = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE html>\n<html>\n  <head>\n    <m[127 chars]l>\n"
            connectionSocket.send(header)
            #Fill in start
            #Fill in end
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found
            #Fill in start
            connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
            #Fill in end
            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data
if __name__ == "__main__":
    webServer(6789)
