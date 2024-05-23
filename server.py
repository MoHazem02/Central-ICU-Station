import socket
import threading
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def start(ui,count):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, address = server.accept()
        handle_client(conn, address, ui,count)
        

def handle_client(conn, address, ui, count):
    print(f"[NEW CONNECTION] {address}")
    while True:
        json_data = conn.recv(4096).decode() 
        print(f"[RECEIVED] {json_data}") 
        reading = json_data[-3:-1]
        reading = int(reading)
        if count == 1:
            ui.Patient1_Heartrate.display(reading)
        if count == 2:
            ui.Patient2_Heartrate.display(reading)
        if count == 3:
            ui.Patient3_Heartrate.display(reading)
        
        time.sleep(1)  

print("[STARTING] server is starting...")

