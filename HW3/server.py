from socket import *

table = ["+", "-", "*", "/"]

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connection from ", addr)
    while True:
        msg = client.recv(1024)
        msg = msg.decode()
        if msg in 'q':
            print("클라이언트와의 연결을 종료합니다.")
            break
        else:
            for i in range(0, len(msg)+1):
                if msg[i] in table:
                    op = msg[i]
                    if msg[i-1] == " ":
                        first = msg[0:i-1]
                    else:
                        first = msg[0:i]
                    if msg[i+1] == " ":
                        second = msg[i+2:]
                    else:
                        second = msg[i+1:]
                    break
            first_number = int(first)
            second_number = int(second)
            if op == "+":
                result = first_number + second_number
            elif op == "-":
                result = first_number - second_number
            elif op == "*":
                result = first_number * second_number
            else:
                result = round(first_number / second_number, 1)
                
            result = str(result)
            client.send(result.encode()) 
    client.close()
    exit()