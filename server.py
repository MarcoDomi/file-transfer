import socket
import threading
import tqdm

host = 'localhost'

def receive_data():
    port = 9091

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.connect((host, port))
    msg = lsock.recv(1024).decode('utf-8')
    print(msg)

port = 9090

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen(2)

s, addr = lsock.accept()
print(f"Connected to client on {addr}")

threading.Thread(target=receive_data, daemon=True).start()

s.send(bytes("Welcome to server",'utf-8'))
s.close()

input("press enter to continue...")