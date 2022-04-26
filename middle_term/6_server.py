import socket
import random

BUF_SIZE = 1024
zero = 0
send = [0 , 0, 0]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7777))
s.listen(2)

while True:
    c, addr = s.accept()
    print("Client connected.")
    while True:
        msg = c.recv(BUF_SIZE)
        msg = msg.decode()
    
        if msg == "1":
            temp = random.randrange(1, 51)
            c.send(temp.to_bytes(12, 'big'))
            print("User: ", msg)
        
        elif msg == "2":
            hum = random.randrange(1, 101)
            c.send(hum.to_bytes(12, 'big'))
            print("User: ", msg)
        
        elif msg == "3":
            lu = random.randrange(1, 151)
            c.send(lu.to_bytes(12, 'big'))
            print("User: ", msg)