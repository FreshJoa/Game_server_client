import socket
from _thread import *
import sys


#bind() służy do powiązania gniazda z określonym interfejsem sieciowym i numerem portu:
#Argumenty przekazane w celu socket()określenia rodziny adresów i typu gniazda. AF_INETto rodzina adresów internetowych dla IPv4
# . SOCK_STREAMjest typem gniazda dla protokołu TCP

# listen() enables a server to accept() connections. It makes it a “listening” socket
#accept() blokuje i czeka na połączenie przychodzące. Gdy klient się łączy, zwraca nowy obiekt gniazda reprezentujący połączenie i
# krotkę zawierającą adres klienta. Krotka będzie zawierać (host, port)

server = ""

port = 5555 # Port to listen on (non-privileged ports are > 1023)


socekt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((server, port))
except socket.error as e:
    #str() convert number into the string
    str(e)


socket.listen(2) #two people
print("Waiting for connection")


def threaded_client(conn):
    pass

while True:
    conn, addr = socket.accept()
    print("Connected with: ", addr)

    start_new_thread(threaded_client, conn)
