import socket
from _thread import *
import sys


#bind() służy do powiązania gniazda z określonym interfejsem sieciowym i numerem portu:
#Argumenty przekazane w celu socket()określenia rodziny adresów i typu gniazda. AF_INETto rodzina adresów internetowych dla IPv4
# . SOCK_STREAMjest typem gniazda dla protokołu TCP

# listen() enables a server to accept() connections. It makes it a “listening” socket
#accept() blokuje i czeka na połączenie przychodzące. Gdy klient się łączy, zwraca nowy obiekt gniazda reprezentujący połączenie i
# krotkę zawierającą adres klienta. Krotka będzie zawierać (host, port)




server = "10.2.77.160"

port = 5555 # Port to listen on (non-privileged ports are > 1023)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    #str() convert number into the string
    str(e)


s.listen(2) #two people
print("Waiting for connection")


def read_pos(str):
    str=str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos=[(0,0), (100, 100)]

#conn.recv(). This reads whatever data
# the client sends and echoes it back using conn.sendall().
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = " "
    while True:
        try:
            data=read_pos(conn.recv(2048).decode())
            #reply = data.decode("utf-8")
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply=pos[1]

                print("Received ", data)
                print("Sending ", reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()

#encode() method, you can convert unicoded strings into
# any encodings supported by Python. By default, Python uses utf-8 encoding.

currentPlayer = 0


while True:
    conn, addr = s.accept()
    print("Connected with: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1