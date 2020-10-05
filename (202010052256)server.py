import socket, sys
import random
import threading
import time
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse tcp
sock.bind(('192.168.0.102', 54321))
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
            msg_1 = csock.recv(1024).decode("utf-8")
            if os.path.isfile('Raidcall/UserData/'+msg_1):
                csock.send('please give me password'.encode(encoding='utf_8',errors='strict'))
                msg_2 = csock.recv(1024).decode("utf-8")
                f = open('Raidcall/UserData/'+msg_1, 'r+')
                if f.readline().replace('\n','')==msg_2:
                    if (str(([k for k, v in connectionIDlist.items() if v == msg_1])).replace('[','').replace(']','').replace('\'','') in connectionIDlist)==True:
                        del connectionIDlist[[k for k, v in connectionIDlist.items() if v == 'a1c5d4g'][0]]
                    connectionID=chr(random.randrange(32,126,1))+str(random.randrange(1,2147483647,1))
                    connectionIDlist[connectionID]=msg_1
                    f.close()
                    csock.send(connectionID.encode(encoding='utf_8',errors='strict'))
                else:
                    csock.send('Login Failed'.encode(encoding='utf_8',errors='strict'))
            else:
                csock.send('Login Failed'.encode(encoding='utf_8',errors='strict'))
            csock.close()
        elif msg == 'reg':
            csock.send('please give username'.encode(encoding='utf_8',errors='strict'))
            temp_username = csock.recv(1024).decode("utf-8")
            if (temp_username == ''):
                csock.close()
                continue
            csock.send('please give password'.encode(encoding='utf_8',errors='strict'))
            temp_password = csock.recv(1024).decode("utf-8")
            if (temp_password == ''):
                csock.close()
                continue
            if os.path.isfile('Raidcall/UserData/'+temp_username):
                csock.send('user has been registed'.encode(encoding='utf_8',errors='strict'))
                csock.close()
                continue
            f = open('Raidcall/UserData/'+temp_username, 'w+')
            f.write(temp_password)
            f.close()
            csock.close()
        elif msg == 'init':
            print(str(adr)+"Trying get user data")
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            temp_conID = csock.recv(1024).decode("utf-8")
            if temp_conID == '':
                csock.close()
                continue
            else:
                f = open('Raidcall/UserData/'+connectionIDlist[temp_conID],'r+')
                f.readline()
                Data = f.readline()
                f.close()
                if Data=='':
                    temp_dict = {'Image':'https://drive.google.com/file/d/1ApcdmJw8EhZl55qGMo87MbBrDRFFV8RK/view?usp=sharing','Name':connectionIDlist[temp_conID],'StatusBar':'empty','FriendList':['empty'],'InArea':'empty'}
                    f = open('Raidcall/UserData/'+connectionIDlist[temp_conID],'r+')
                    temp_info = f.read()
                    f.write(temp_info+'\n'+str(temp_dict))
                    f.close()
                    Data = str(temp_dict)
                csock.send(Data.encode(encoding='utf_8',errors='strict'))
                csock.close()
        elif msg == 'connect RC group':
            print(str(adr)+"Trying connect RC group")
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            temp_conID = csock.recv(1024).decode("utf-8")
            if temp_conID == '':
                csock.close()
                continue
            temp_user = connectionIDlist[temp_conID]
            csock.send('please give RCGroupID'.encode(encoding='utf_8',errors='strict'))
            temp_RCGID = csock.recv(1024).decode("utf-8")
            if temp_RCGID == '':
                csock.close()
                continue
            if not os.path.isfile('Raidcall/RaidcallGroups/'+temp_RCGID):
                csock.close()
                continue
            f = open('Raidcall/RaidcallGroups/'+temp_RCGID,'r+')
            temp_GD = eval(f.read())
            for a in temp_GD['channels']:
                if not(temp_user in temp_GD['roles']['black']) or (temp_user in temp_GD['roles']['purple']):
                    if a['IIC'] == True:
                        a['peoples'] = a['peoples']+[temp_user]
                        temp_GD['groupdata']['peoples']+=1
                else:
                    csock.send('You are black list of this RC group'.encode(encoding='utf_8',errors='strict'))
                    csock.close()
                    continue
            f.close()
            f = open('Raidcall/RaidcallGroups/'+temp_RCGID,'w+')
            f.write(str(temp_GD))
            print(str(temp_GD))
            f.close()
            csock.close()
        elif msg == 'RC group data'
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            temp_conID = csock.recv(1024).decode("utf-8")
            if temp_conID == '':
                csock.close()
                continue
            temp_user = connectionIDlist[temp_conID]
            csock.send('please give RCGroupID'.encode(encoding='utf_8',errors='strict'))
            temp_RCGID = csock.recv(1024).decode("utf-8")
            temp_check_bool_var_01 = False
            if temp_RCGID == '':
                csock.close()
                continue
            if not os.path.isfile('Raidcall/RaidcallGroups/'+temp_RCGID):
                csock.close()
                continue
            f = open('Raidcall/RaidcallGroups/'+temp_RCGID,'r+')
            temp_GD = eval(f.read())
            for temp_check_var_channel in temp_GD['channels']:
                for temp_check_var_user in temp_GD['channels'][temp_check_var_channel][peoples]:
                    if temp_check_var_user==temp_user:
                        temp_check_bool_var_01 = True
                        break
            if temp_check_bool_var_01 = True:
                csock.send(str(temp_GD).encode(encoding='utf_8',errors='strict'))
                csock.close()
            else:
                csock.send('you are not in group'.encode(encoding='utf_8',errors='strict'))
                csock.close()
                continue
        elif msg == 'switch channel':
            csock.send('please give connectionID'.encode(encoding='utf_8',errors='strict'))
            ##識別connectionID是屬於哪一個user
            temp_conID = csock.recv(1024).decode("utf-8")
            if temp_conID == '':
                csock.close()
                continue
            temp_user = connectionIDlist[temp_conID]
            csock.send('please give RCGroupID'.encode(encoding='utf_8',errors='strict'))
            temp_RCGID = csock.recv(1024).decode("utf-8")
            temp_check_bool_var_01 = False
            if temp_RCGID == '':
                csock.close()
                continue
            if not os.path.isfile('Raidcall/RaidcallGroups/'+temp_RCGID):
                csock.close()
                continue
            f = open('Raidcall/RaidcallGroups/'+temp_RCGID,'r+')
            temp_GD = eval(f.read())
            for temp_check_var_channel in temp_GD['channels']:
                for temp_check_var_user in temp_GD['channels'][temp_check_var_channel][peoples]:
                    if temp_check_var_user==temp_user:
                        temp_check_bool_var_01 = True
                        break
            if temp_check_bool_var_01 = True:
                csock.send('which channel will you go?'.encode(encoding='utf_8',errors='strict'))
                temp_sw_ch_var = csock.recv(1024).decode("utf-8")
                if temp_sw_ch_var == '':
                    csock.close()
                    continue
                if [temp_sw_ch_var] in temp_GD['channels']:
                    #[...]
                csock.close()
            else:
                csock.send('you are not in group'.encode(encoding='utf_8',errors='strict'))
                csock.close()
                continue
        else:
            print("Breaking Error Connect:"+str(adr))
            csock.send('Server Break A Error Connect'.encode(encoding='utf_8',errors='strict'))
            csock.close()
connect_dic={}
max_connect=10
temp_int1=0
while temp_int1<=max_connect:
    connect_dic["a"+str(temp_int1)]=threading.Thread(target=i)
    connect_dic["a"+str(temp_int1)].start()
    temp_int1+=1
    
