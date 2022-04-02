from socket import *
import sys

BUFFSIZE = 1024
port = 3000
dic = {}

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 3000))

while True:
    data, addr = s.recvfrom(BUFFSIZE)
    data = data.decode()
    msg = data.split(" ", maxsplit=3)
    if msg[0] == "send":
        dic[msg[1]] = msg[2]
        s.sendto("OK".encode(), addr)
    elif msg[0] == "receive":
        if msg[1] in dic.keys():
            s.sendto(dic[msg[1]].encode(), addr)
        else:
            s.sendto("No messages".encode(), addr)    
    elif msg[0] == "quit":
        print("quit")
        s.close()
        sys.exit()
        
    else:
        s.sendto("다시 입력해주세요.".encode(), addr)
        