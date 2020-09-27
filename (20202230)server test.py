import socket, sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind(('127.0.0.1', 54321))
sock.listen(5)


while True:
    (csock, adr) = sock.accept()
    msg = csock.recv(1024).decode("utf-8")
    if not msg == 'connect raidcall server':
        print("Format Error Client: "+str(adr))
        b = '[ERROR]The connect request message you send can\'t be understand in server.'
        csock.send(b.encode(encoding='utf_8',errors='strict'))
        
    else:
        print("Client Connect: "+str(adr))
        a = 'sucessful connected!'
        a = a.encode(encoding='utf_8',errors='strict')
        csock.send(a)
        msg = (csock.recv(1024)).decode("utf-8")
        msg = msg+str(random.randrange(0, 99999,1))
        msg = msg.encode('utf_8',errors='strict')
        csock.send(msg)
        csock.close()
        continue
    csock.close()
