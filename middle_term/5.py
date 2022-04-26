import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(10)

def handler(c, addr):
    data = c.recv(2048)
    msg = data.decode()
    req = msg.split("\r\n")
    index = req[0].split(' ')
    route = index[1]
    filename = route[1:]
    print(filename)
    
    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'

        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data.encode('euc-kr'))
        print("HTML 전송 완료")
    
    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'

        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data)
        print("IMAGE 전송 완료")
        
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        data = 'Content-Type: ' + mimeType + '\r\n'
        c.send(data.encode())
        c.send('\r\n'.encode())
        data =  f.read()
        c.send(data)
        print("ICON 전송 완료")
        
    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())
        print("404 Not Found")
        
    c.close()

while True:
    c, addr = s.accept()
    th = threading.Thread(target=handler, args=(c, addr))
    th.daemon = True
    th.start()
    