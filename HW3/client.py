from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input("계산하고 싶은 수식을 입력하세요: ")
    if msg == 'q':
        print("서버와의 연결을 종료합니다.")
        break
    
    s.send(msg.encode())
    result = s.recv(1024)
    
    print(result.decode())
    
s.close()