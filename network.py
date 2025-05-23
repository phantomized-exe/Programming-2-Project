import socket
global rand_ip
rand_ip = -1

def get_server_ip():
    global rand_ip
    rand_ip += 1
    return f"192.168.0.{rand_ip}"
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = get_server_ip
        self.port = 12345
        self.addr = (self.server,self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(f"Error: {e}")

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

