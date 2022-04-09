from socket import *
import random

BUFFSIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print("Listening...")

while True:
    data, addr = s_sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 3:
        print("Packet is {} from lost!".format(addr))
        continue
    print("Packet is {} from {}.".format(data.decode(), addr))
    
    s_sock.sendto("ack".encode(), addr)