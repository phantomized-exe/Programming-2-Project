import socket

def get_local_ip():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect(('8.8.8.8', 80)) 
            return sock.getsockname()[0]
        except:
            return '127.0.0.1'
        finally:
            sock.close()

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = f"{get_local_ip()}"
        self.port = 12345
        self.addr = (self.server,self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            network_ip = input("Enter server IP: ")
            try:
                self.addr = (network_ip,self.port)
                self.pos = self.connect
            except Exception as e:
                print(f"Error: {e}")

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

