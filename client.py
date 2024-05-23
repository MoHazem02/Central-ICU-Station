import socket
import random
import time
import json


PORT = 5050
SERVER = "192.168.1.5"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(hr):
    json_data = {
        "HR": hr,
    }

    json_string = json.dumps(json_data)
    client.sendall(json_string.encode())


def send_vital_signal():
    hr = random.randint(60, 99)

    msg = f"HR: {hr}"
    send(hr)
    print(f"[SENT] {msg}")


while True:
    send_vital_signal()
    time.sleep(1)
