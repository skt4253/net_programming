from socket import *
import sys
import time

BUF_SIZE = 1024
LENGTH = 6

dv1 = socket(AF_INET, SOCK_STREAM)
dv1.bind(('', 3000))
dv2 = socket(AF_INET, SOCK_STREAM)
dv2.bind(('', 4000))
dv1.listen(10)
dv2.listen(10)

f = open("data.txt", 'a')

while True:
    con1, addr1 = dv1.accept()
    con2, addr2 = dv2.accept()
    print("Device connected.")
    while True:
        msg = input(">> ")
        if not msg:
            continue
        if msg == "1":
            req = con1.send("Request".encode())
            rec = con1.recv(BUF_SIZE)
            t = int.from_bytes(rec, 'big')
            rec = con1.recv(BUF_SIZE)
            h = int.from_bytes(rec, 'big')
            rec = con1.recv(BUF_SIZE)
            l = int.from_bytes(rec, 'big')
            print(t, h, l)
            f.write(time.ctime(time.time()) + ": Dvice1: Temp={}, Humid={}, lilum={}\n".format(t, h, l))
        if msg == "2":
            req = con2.send("Request".encode())
            rec = con2.recv(BUF_SIZE)
            he = int.from_bytes(rec, 'big')
            rec = con2.recv(BUF_SIZE)
            s = int.from_bytes(rec, 'big')
            rec = con2.recv(BUF_SIZE)
            c = int.from_bytes(rec, 'big')
            print(he, s, c)
            f.write(time.ctime(time.time()) + ": Dvice2: Heartbeat={}, Steps={}, Cal={}\n".format(he, s, c))
        elif msg == "quit":
            req = con1.send("quit".encode())
            f.close()
            con1.close()
            sys.exit()
