import socket
import pickle

#class responsible for connecting to  the server
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.68.18.84"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
    #return position
    def getP(self):
        return self.p

    def connect(self):
        try:
            #if connect  it sends some kind of information immediately back to the object that connected to us
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            #send what  it gots right back
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)