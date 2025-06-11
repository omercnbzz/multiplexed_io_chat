import selectors
import socket

sel= selectors.DefaultSelector()
def accept(sock, mask):
    conn, addr = sock.accept()
    print("Accepted connection from",addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)
    
def read(conn, mask):
    data=conn.recv(1000)
    if data:
        print("Recevied data",repr(data),'from',conn)
    else:
        print('Closing connection',conn)
        sel.unregister(conn)
        conn.close()

sock =socket.socket()
sock.blind('localhost',1234)
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)

while True:
    events=set.select()
    for key,mask in events:
       callback=key.data
       callback(key.fileobj,mask)
     