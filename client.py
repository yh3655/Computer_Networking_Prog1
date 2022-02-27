#import socket module
from socket import *
import sys # In order to terminate the program

def webClient():
    server_host = sys.argv[1]
    #print(server_host)
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_host,server_port))
        header = ("GET /%s HTTP/1.1" %(filename)).encode()
        client_socket.send(("%s \r\n\r\n" %header).encode())

    except IOError:
        sys.exit()
    response_message = client_socket.recv(1024)
    result = ""
    while response_message:
        result += response_message.decode()
        response_message = client_socket.recv(1024)
    client_socket.close()
    print(result)








if __name__ == "__main__":
    webClient()