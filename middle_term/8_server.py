from socket import *
import select

BUFFSIZE = 1024
port = 3000
dic = {}
socks = []

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3000))
s.listen(5)

socks.append(s)

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    
    for c in r_sock:
        if c == s:
            sock, addr = s.accept()
            socks.append(sock)
            print("Client ({}) connected.".format(addr))
        else:
            data = sock.recv(BUFFSIZE)
            if not data:
                continue
            data = data.decode()
            msg = data.split(" ", maxsplit=3)
            if msg[0] == "send":
                dic[msg[1]] = msg[2]
                sock.send("OK".encode())
            elif msg[0] == "receive":
                if msg[1] in dic.keys():
                    sock.send(dic[msg[1]].encode())
                else:
                    sock.send("No messages".encode())    
            elif msg[0] == "quit":
                print(addr+ " quit")
                sock.close()
        
            else:
                sock.send("다시 입력해주세요.".encode())
        