import socket as sc
import threading

HEADER = 64 #length of the message
PORT = 9999
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT) # ADDR for socket ; socket = ip address + port number
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "[DISCONNECTED]"

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM) # AF_INET is for IPv4 and SOCk_STREAM represents Tcp connection
server.bind(ADDR)


    

def handle_client(conn, addr) :
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # recives the message length
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # the actual message

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]  {msg}")
            s = f"[MESSAGE RECIVED] {addr}"
            message = s.encode(FORMAT)
            conn.send(message)
            

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # gives info about rhe client and its address
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # creating a new thread for each client 
        thread.start() 
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # getting the active clients 

print("[STARTING] server is starting... ")
start()
