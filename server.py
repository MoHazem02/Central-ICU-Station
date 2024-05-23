import socket
import threading
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, address = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, address))
        thread.start()
        

def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} ")
    while True:
        json_data = conn.recv(4096).decode() 
        print(f"[RECEIVED] {json_data}") 
        time.sleep(1)  

print("[STARTING] server is starting...")
start()
