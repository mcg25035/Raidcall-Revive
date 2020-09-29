import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 54321
client.connect((host, port))
sendmsg = input("請輸入:")
client.send(sendmsg.encode("utf-8",errors='strict'))
msg = client.recv(1024)
msg = msg.decode("utf-8")
if msg == 'sucessful connected!':
    sendmsg = input("請輸入:")
    client.send(sendmsg.encode("utf-8",errors='strict'))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
else:
    print('connect not successful!')
client.close()
