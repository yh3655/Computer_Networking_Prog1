from socket import *
import threading


class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)  # Fill in start #Fill in end
                print("Message: ", message)
                filename = message.split()[1]
                print(filename)
                f = open(filename[1:])
                outputdata = f.read()  # Fill in start #Fill in end
                # Send one HTTP header line into socket
                header = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                connectionSocket.send(header)
                # Fill in start
                # Fill in end
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                #connectionSocket.close()
            except IOError:
                # Send response message for file not found
                # Fill in start
                connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
                # Fill in end
                # Close client socket
                # Fill in start
                #connectionSocket.close()
                # Fill in end



if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a server socket
    #Fill in start
    serverport = 6789
    #HOST = '192.168.31.230'
    serverSocket.bind(("",serverport))
    serverSocket.listen()
    threads = []
    # Fill in end
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        # Fill in start
        # Fill in end
        client_thread = ClientThread(connectionSocket, addr)
        client_thread.setDaemon(True)
        client_thread.start()
        threads.append(client_thread)

    # main thread wait all threads finish then close the connection
    for thread in threads:
     	thread.join()
    serverSocket.close()