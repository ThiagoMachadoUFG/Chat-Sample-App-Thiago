from socket import *
import pickle
import const
import threading

def handle_client(conn, addr):
    try:
        marshaled_msg_pack = conn.recv(1024)  # receive data from client
        msg_pack = pickle.loads(marshaled_msg_pack)
        type = msg_pack[0]
        print(type)
        conn.send(pickle.dumps("ACK"))  # send ACK to client
        conn.close()

server_sock = socket(AF_INET, SOCK_STREAM)  # socket for clients to connect to this server
server_sock.bind(('0.0.0.0', const.CHAT_SERVER_PORT))
server_sock.listen(5)  # may change if too many clients

print("Chat Server is ready...")

while True:
    try:
        (conn, addr) = server_sock.accept()  # returns new socket and addr. client
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
    except KeyboardInterrupt:
        break

server_sock.close()
