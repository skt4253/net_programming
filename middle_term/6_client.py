from socket import *
import sys
import time

BUF_SIZE = 1024
LENGTH = 4

svr_addr = ("localhost", 7777)
c = socket(AF_INET, SOCK_STREAM)
c.connect(svr_addr)

while True:
    print("Server connected.")
    while True:
        msg = input(">> ")

        if msg == "1":
            req = c.send("1".encode())
            rec = c.recv(BUF_SIZE)
            t = int.from_bytes(rec, 'big')
            print("Temp={}, Humid=0, Lumi=0".format(t))

        if msg == "2":
            req = c.send("2".encode())
            rec = c.recv(BUF_SIZE)
            h = int.from_bytes(rec, 'big')
            print("Temp=0, Humid={}, Lumi=0".format(h))

        if msg == "3":
            req = c.send("3".encode())
            rec = c.recv(BUF_SIZE)
            l = int.from_bytes(rec, 'big')
            print("Temp=0, Humid=0, Lumi={}".format(l))

