from socket import *
import random
import time

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

while True:
    msg = input('-> ') # 송신
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)
        
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    sock.settimeout(None)
    while True: # 수신
        data, addr = sock.recvfrom(BUFFSIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b"ack", addr)
            print("<- ", data.decode())
            break

       