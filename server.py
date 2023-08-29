import socket
import threading
import tqdm


def receive_data(sock):
    print('check')
    while True:
        print('check1')
        msg = sock.recv(1024).decode('utf-8')
        print('check')
        print(msg)

host = 'localhost'
port = 9090

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))

lsock.listen(2)

#while True:
s, addr = lsock.accept()
print(f"Connected to client on {addr}")
threading.Thread(target=receive_data, daemon=True, args=(s,)).start()

input("press enter to continue...")