import socket
import threading
import tqdm

host = 'localhost'

def receive_data():
    port = 9090
   
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.connect((host, port))
    while True:
        msg = lsock.recv(1024).decode('utf-8')
        if msg != "":
            print(msg)
        else:
            lsock.close()
            break

threading.Thread(target=receive_data, daemon=True).start()

port = 9091

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen(2)

s, addr = lsock.accept()
print(f"Connected to client on {addr}")

while True:
    s.send(bytes("Hello from client",'utf-8'))
    next = input("Send another file?[y/n]")
    if next == 'n':
        s.close()
        break




