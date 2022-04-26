from socket import *
import time

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

# 송신
reTx = 0
sendTime = time.time()
while reTx <= 3:
    sock.sendto("ping".encode(), ('localhost', port))
    print("ping")
    sock.settimeout(2) 
        
    try:
        data, addr = sock.recvfrom(BUFFSIZE)

    except timeout:
        if reTx == 2 :
            print("Fail")
            sock.close()
            break
        reTx += 1
        continue
    else:
        if data.decode() == "pong":
            recvTime = time.time()

            print("Success (RTT: {})".format(recvTime - sendTime))
            sock.close()
            break
       