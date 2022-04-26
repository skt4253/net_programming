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
        if not data:
            break
        
        if random.random() <= 0.5:
            print("Fail")
            continue
        else:
            sock.sendto("pong".encode(), addr)
            print("Send pong")
            break