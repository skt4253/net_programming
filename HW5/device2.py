from socket import *
import sys
import random

BUF_SIZE = 1024
LENGTH = 700

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4000))

while True:
    msg = s.recv(BUF_SIZE)
    msg = msg.decode()
    if not msg:
        s.close()
        sys.exit()
    if msg == "Request":
        he = random.randrange(40, 141)
        print(he)
        se = random.randrange(2000, 6001) 
        c = random.randrange(1000, 4001)
        s.send(he.to_bytes(LENGTH, 'big'))
        s.send(se.to_bytes(LENGTH, 'big'))
        s.send(c.to_bytes(LENGTH, 'big'))
        print("User: ", msg)
    elif msg == "quit":
        print("연결 종료")
        s.close()
        sys.exit()
    else:
        print("User: ", msg)