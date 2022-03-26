import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

msg = "Sujin Yoo"
sock.send(msg.encode())
msg = sock.recv(1024)
print(int.from_bytes(msg, 'big'))
sock.close()