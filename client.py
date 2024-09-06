import socket as sc

HEADER = 64 #length of the message
PORT = 9999
DISCONNECT_MESSAGE = "[DISCONNECTED]"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT) # ADDR for socket ; socket = ip address + port number
FORMAT = 'utf-8'

client = sc.socket(sc.AF_INET, sc.SOCK_STREAM) # AF_INET is for IPv4 and SOCk_STREAM represents Tcp connection
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) # encoding the message
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # encoding the length of the message
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello from ASH")
send("How are you doing ?")
send("Did you complete the task ?")
send(DISCONNECT_MESSAGE)