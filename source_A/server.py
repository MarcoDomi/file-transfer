import socket
import threading
import tqdm
import os

host = 'localhost'

def receive_data():
    port = 9091

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.connect((host, port))
    msg = lsock.recv(1024).decode('utf-8')
    print('check')
    print(msg)

port = 9090

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen(2)

s, addr = lsock.accept() #this will block the program while waiting for connection
print(f"Connected to client on {addr}")

threading.Thread(target=receive_data, daemon=True).start()

#file_name = "sendme.txt"
#file = open(file_name,"rb")
#file_size = os.path.getsize(file_name)

s.send(bytes("Welcome to server",'utf-8'))

s.close()
