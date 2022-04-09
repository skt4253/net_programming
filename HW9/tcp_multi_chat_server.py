import socket
import time
import threading

thread = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2500))
s.listen(3)

print("Server Started")
   
def handler(sock, addr):
    while True:
        data = sock.recv(1024)
        # quit을 수신하면 해당 클라이언트를 목록에서 삭제
        if "quit" in data.decode():
            if sock in thread:
                print(addr, 'exited')
                thread.remove(sock)
                continue
        
        # 새로운 클라이언트면 목록에 추가
        if sock not in thread:
            print("new client", addr)
            thread.append(sock)
        
        print(time.asctime() + str(addr) + ':' + data.decode())
    
        # 모든 클라이언트에게 전송
        for client in thread:
            if client != sock:
                client.send(data)

while True:
    sock, addr = s.accept()
    th = threading.Thread(target=handler, args=(sock, addr))
    th.start()
    