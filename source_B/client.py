import socket
import threading
import tqdm
import os

host = 'localhost'

def receive_data():
    port = 9090
   
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.connect((host, port))
   
    while True:
        file_name = lsock.recv(1024).decode('utf-8')
        file_size = lsock.recv(1024).decode('utf-8')
        #recv_file = lsock.recv(1024).decode('utf-8')
        print(file_name)
        print(file_size)
        file = open(file_name, "wb")
        prog_bar = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000,
                        total=int(file_size))
        file_bytes = b""
        done = False
        while not done:
            data = lsock.recv(1024)
           
            if file_bytes[-5:] == b"<END>" or data[-5:] == b"<END>":
                done = True
            #else:
            file_bytes += data
            prog_bar.update(1024)
        
        file.write(file_bytes[:-5])
        file.close()
        break
    lsock.close()
    

threading.Thread(target=receive_data, daemon=True).start()

port = 9091

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen(2)

s, addr = lsock.accept()
print(f"Connected to client on {addr}")


file_name = "fish.jpg"
file = open(file_name,"rb")
file_size = os.path.getsize(file_name)

s.send(bytes(file_name,'utf-8'))
s.send(bytes(str(file_size),'utf-8'))

data = file.read()
data += b"<END>"
s.sendall(data)

file.close()

input("press enter to continue")
    
