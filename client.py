import socket

host = 'localhost'
port = 9090

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.connect((host, port))