from socket import *

BUFFSIZE = 1024
port = 3000

c = socket(AF_INET, SOCK_DGRAM)
c.connect(('localhost', port))

while True:
    data = input("Enter the message(\"send mboxId message\" of \"receive mboxId\"): ")
    if data in "quit":
        break
    c.send(data.encode())
    msg = c.recv(BUFFSIZE)
    
    print(msg.decode())
    
c.close()
    