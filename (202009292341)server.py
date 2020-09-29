import socket, sys
import random
import threading
import time
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind(('127.0.0.1', 54321))
sock.listen(5)
connectionIDlist={}
def i():
    global connectionIDlist
    while True:
        (csock, adr) = sock.accept()
        msg = csock.recv(1024).decode("utf-8")
        if msg == 'login':
            print(str(adr)+"Trying Login!")
            csock.send('please give me username'.encode(encoding='utf_8',errors='strict'))
            ##login
            msg_1 = csock.recv(1024).decode("utf-8")
            if os.path.isfile('Raidcall/UserData/'+msg_1):
                csock.send('please give me password'.encode(encoding='utf_8',errors='strict'))
                msg_2 = csock.recv(1024).decode("utf-8")
                f = open('Raidcall/UserData/'+msg_1, 'r+')
                if f.read()==msg_2:
                    if (str(([k for k, v in connectionIDlist.items() if v == msg_1])).replace('[','').replace(']','').replace('\'','') in connectionIDlist)==True:
                        del connectionIDlist[[k for k, v in connectionIDlist.items() if v == msg1]]
                    connectionID=chr(random.randrange(32,126,1))+str(random.randrange(1,2147483647,1))
                    connectionIDlist[connectionID]=msg_1
                    f.close()
                    csock.send(connectionID.encode(encoding='utf_8',errors='strict'))
                else:
                    csock.send('Login Failed'.encode(encoding='utf_8',errors='strict'))
            else:
                csock.send('Login Failed'.encode(encoding='utf_8',errors='strict'))
            csock.close()
        elif msg == 'get user data':
            print(str(adr)+"Trying get user data")
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            csock.recv(1024).decode("utf-8")
            csock.close()
        elif msg == 'connect RC group':
            print(str(adr)+"Trying connect RC group")
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            csock.recv(1024).decode("utf-8")
            csock.close()
        else:
            print("Breaking Error Connect:"+str(adr))
            csock.send('Server Break A Error Connect'.encode(encoding='utf_8',errors='strict'))
            csock.close()
            continue
        csock.close()
connect_dic={}
max_connect=10
temp_int1=0
while temp_int1<=max_connect:
    connect_dic["a"+str(temp_int1)]=threading.Thread(target=i)
    connect_dic["a"+str(temp_int1)].start()
    temp_int1+=1
    
