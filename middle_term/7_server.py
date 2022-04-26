import socket, selectors
import time

sel = selectors.DefaultSelector()

select = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 2500))
sock.listen(3)

print("Server Started")
                
def accept(sock, mask):
    # 새로운 클라이언트면 목록에 추가
    conn ,addr = sock.accept()
    select.append(conn)
    sel.register(conn, selectors.EVENT_READ, read)
    # if r_sock not in thread:
    #     print("new client", addr)
    #     thread.append(r_sock)

def read(conn, mask):
    data = conn.recv(1024)
    print(time.asctime() + ':' + data.decode())
    if not data:
        sel.unregister(conn)
        return
        # quit을 수신하면 해당 클라이언트를 목록에서 삭제
    if "quit" in data.decode():
        sel.unregister(conn)
        select.remove(conn)
        conn.close()
    for client in select:
        if conn != client:
            client.send(data)
            
sel.register(sock, selectors.EVENT_READ, accept)
while True:
    event = sel.select()
    for key, mask in event:
        callback = key.data
        callback(key.fileobj, mask)