from threading import Thread
import socket

IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():

    print("\n\t\t\t\t\t\ IP MESSENGER\n")

    
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\n\t\t\t\t SERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()


def acceptConnections():
    global SERVER
    global clients

    while True:
        clients, addr = SERVER.accept()
        print('client.addr')