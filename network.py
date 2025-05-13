import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "10.30.51.115" #ipconfig in command prompt, home ip: 172.16.0.2, school ip: due to vpn needs to be configured
        self.port = 5555
        self.addr = (self.server,self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

