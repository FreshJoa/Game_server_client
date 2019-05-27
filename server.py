#!/home/mazurek/anaconda3/bin/python
import socket
from _thread import *
from player import Player
import pickle
import sys

server = "10.68.18.84"

port = 5555 # Port to listen on (non-privileged ports are > 1023)

#socket.socket() creates a socket object that supports the context manager type
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #bind() is used to associate the socket with a specific network interface and port number
    s.bind((server, port))
except socket.error as e:
    #str() convert number into the string
    str(e)

#listen() has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections. 
s.listen(2)
print("Waiting for connection")
#create two players
players=[Player(600, 600, 'X'),Player(600, 600, 'O')]




#conn.recv(). This reads whatever data
# the client sends and echoes it back using conn.sendall().
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            #pickle.loads Read a pickled object hierarchy from a bytes object and return the reconstituted object hierarchy specified therein.
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)
            #pickle.dumps Return the pickled representation of the object as a string, instead of writing it to a file.
            #conn.sendall eads whatever data the client sends and echoes it back
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    #ends the connection
    conn.close()

currentPlayer = 0
while True:
    #accept When a client connects, the server calls accept() to accept, or complete, the connection.
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
