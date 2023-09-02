import socket
import threading
import tqdm
import os

host = 'localhost'

def receive_data():
    port = 9091

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.connect((host, port))
    while True:
        msg = lsock.recv(1024).decode('utf-8')
        if msg != "":
            print(msg)
        else:
            lsock.close()
            break

port = 9090

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen(2)

s, addr = lsock.accept() #this will block the program while waiting for connection
print(f"Connected to client on {addr}")
threading.Thread(target=receive_data, daemon=True).start()
#TODO create a list of file names to send
while True:
    file_name = "sendme.txt"
    file = open(file_name,"rb")
    file_size = os.path.getsize(file_name)

    s.send(bytes(file_name, 'utf-8'))
    s.send(bytes(str(file_size),'utf-8'))

    data = file.read()
    data += b"<END>"
    print(data)
    s.sendall(data)
   
    file.close()

    input("press enter to continue")
    '''
    next = input("Send another file?[y/n]")
    if next == 'n':
        s.close()
        break
        '''

