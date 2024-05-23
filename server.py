import socket
import threading
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def start(ui):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, address = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, address, ui))
        thread.start()
        

def handle_client(conn, address, ui):
    print(f"[NEW CONNECTION] {address}")
    while True:
        json_data = conn.recv(4096).decode() 
        print(f"[RECEIVED] {json_data}") 
        reading = int(json_data[-2 :])
        ui.Patient1_Heartrate.display(reading)
        ui.Patient2_Heartrate.display(reading)
        ui.Patient3_Heartrate.display(reading)
        
        time.sleep(1)  

print("[STARTING] server is starting...")
start()
