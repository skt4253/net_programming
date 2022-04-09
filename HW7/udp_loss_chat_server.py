from socket import *
import random
import time

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("", port))

while True:
    sock.settimeout(None) # 수신
    while True:
        data, addr = sock.recvfrom(BUFFSIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b"ack", addr)
            print("<- ", data.decode())
            break
        
    msg = input('-> ') # 송신
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break