import socket
import random
from _thread import *
#import sys
def get_local_ip():
    """finds the ip clients must connect to

    Returns:
        str: returns the ip
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('8.8.8.8', 80)) 
        return sock.getsockname()[0]
    except:
        return '127.0.0.1'
    finally:
        sock.close()
server = "0.0.0.0" #ipconfig in command prompt
port = 12345
connected = [False, False]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))
s.listen(2)

#print("Waiting for a connection, Server Started")
def read_pos(s):
    """reads the values from clients

    Args:
        s (str): the values

    Returns:
        int: returns as a list of ints
    """
    s = s.split(",")
    return int(s[0]), int(s[1]), float(s[2]), s[3]=="True"
def make_pos(tup):
    """formats the data to send back to clients

    Args:
        tup (tup): data

    Returns:
        str: returns formatted data
    """
    return f"{tup[0]},{tup[1]},{tup[2]},{tup[3]}"
pos = [(10000,-10000,0,False),(10000,-10000,0,False)]
def threaded_client(conn, player):
    """decodes info

    Args:
        conn (_type_): _description_
        player (_type_): _description_
    """
    conn.send(str.encode(make_pos(pos[player])))
    while True:
        try:
            raw = conn.recv(2048).decode()
            if not raw:
                print("Client disconnected.")
                pos[player] = (10000,-10000,0,False)
                break
            raw = raw.strip()
            parts = raw.split(",")
            if len(parts) != 4:
                print(f"Player {player+1}: {repr(raw)}")
                continue
            try:
                x = int(parts[0])
                y = int(parts[1])
                vx = float(parts[2])
                crouch = (parts[3] == "True")
            except ValueError as e:
                print(e)
                continue
            pos[player] = (x, y+3, vx, crouch)
            reply = pos[1-player]
            #print(f"Player {player+1}: {pos[player]}; sending back {reply}")
            conn.sendall(str.encode(make_pos(reply)))
        except Exception as e:
            print(f"Player {player+1}: {e}")
            break
    conn.close()
    connected[player] = False
    print(f"Lost connection with player {player+1}")
#currentPlayer = 0
print()
print(f"Clients connect to {get_local_ip()}")
while True:
    conn, addr = s.accept()
    #print("Connected to:", addr)
    #print(f"IP: {addr[0]}\nPort: {addr[1]}")
    #start_new_thread(threaded_client, (conn,currentPlayer))
    #currentPlayer += 1
    player = None
    for i in range(2):
        if not connected[i]:
            player = i
            break
    if player is None:
        print("Server full")
        conn.close()
        continue
    connected[player] = True
    print(f"Player {player+1} connected")
    start_new_thread(threaded_client, (conn, player))