import socket


from _thread import *
import sys


#bind() służy do powiązania gniazda z określonym interfejsem sieciowym i numerem portu:
#Argumenty przekazane w celu socket()określenia rodziny adresów i typu gniazda. AF_INETto rodzina adresów internetowych dla IPv4
# . SOCK_STREAMjest typem gniazda dla protokołu TCP

# listen() enables a server to accept() connections. It makes it a “listening” socket
#accept() blokuje i czeka na połączenie przychodzące. Gdy klient się łączy, zwraca nowy obiekt gniazda reprezentujący połączenie i
# krotkę zawierającą adres klienta. Krotka będzie zawierać (host, port)

server = "10.68.18.84"

port = 5555 # Port to listen on (non-privileged ports are > 1023)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except s.error as e:
    #str() convert number into the string
    str(e)


s.listen(2) #two people
print("Waiting for connection")

#conn.recv(). This reads whatever data
# the client sends and echoes it back using conn.sendall().
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = " "
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received ", reply)
                print("Sending ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()

#encode() method, you can convert unicoded strings into
# any encodings supported by Python. By default, Python uses utf-8 encoding.


while True:
    conn, addr = s.accept()
    print("Connected with: ", addr)

    start_new_thread(threaded_client, (conn,))
