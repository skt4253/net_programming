from socket import *
import sys
import random

BUF_SIZE = 1024
LENGTH = 6

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3000))

while True:
    msg = s.recv(BUF_SIZE)
    msg = msg.decode()
    if not msg:
        s.close()
        sys.exit()
    if msg == "Request":
        t = random.randrange(0, 41)
        h = random.randrange(0, 101) 
        l = random.randrange(70, 151)
        s.send(t.to_bytes(LENGTH, 'big'))
        s.send(h.to_bytes(LENGTH, 'big'))
        s.send(l.to_bytes(LENGTH, 'big'))
        print("User: ", msg)
    elif msg == "quit":
        print("연결 종료")
        s.close()
        sys.exit()
    else:
        print("User: ", msg)