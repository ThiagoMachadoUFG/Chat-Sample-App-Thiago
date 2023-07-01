from socket import *
import pickle
import const
import threading
import json

file_path = 'users.json'
users = {}

try:
    with open(file_path, 'r') as file:
        contents = file.read()
        if contents:
            users = json.loads(contents)
except (FileNotFoundError, json.JSONDecodeError):
    pass

def handle_client(conn, addr):
    try:
        marshaled_msg_pack = conn.recv(1024)  # receive data from client
        msg_pack = pickle.loads(marshaled_msg_pack)
        type = msg_pack[0]
        if type=="auth":
            conn.send(pickle.dumps("ACK"))  # send ACK to client
            conn.close()
            name=msg_pack[1]
            users[name]=addr[0]
        elif type=="msge":
            print("msge")
            
    except Exception as e:
        print("Error handling client:", e)

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
with open(file_path, 'w') as file:
    json.dump(users, file)
