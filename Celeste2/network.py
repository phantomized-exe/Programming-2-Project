import socket

class Network:
    def __init__(self,server_ip):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = server_ip
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

