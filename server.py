import socket
from _thread import *
import sys
server = "192.168.0.8" #ipconfig
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    str(e)
s.listen(2)
print("Waiting for a connection, Server Started")
def read_pos(s):
    s = s.split(",")
    return int(s[0]), int(s[1]), float(s[2]), s[3]=="True"
def make_pos(tup):
    return f"{tup[0]},{tup[1]},{tup[2]},{tup[3]}"
pos = [(306,208,0,False),(306,208,0,False)]
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    while True:
        try:
            raw = conn.recv(2048).decode()
            if not raw:
                print("Client disconnected.")
                break
            raw = raw.strip()
            parts = raw.split(",")
            if len(parts) != 4:
                print(f"error player {player!r}: {repr(raw)}")
                continue
            try:
                x = int(parts[0])
                y = int(parts[1])
                vx = float(parts[2])
                crouch = (parts[3] == "True")
            except ValueError as verr:
                print(f"parse error {verr} on {parts}")
                continue
            pos[player] = (x, y, vx, crouch)
            reply = pos[1-player]
            print(f"Player {player+1}: {pos[player]}; sending back {reply}")
            conn.sendall(str.encode(make_pos(reply)))
        except Exception as e:
            print(f"Connection error with player {player+1}: {e}")
            break
    conn.close()
    print(f"Lost connection with player {player}")
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer += 1