from socket import *
import pickle
import const
import threading

server_sock = socket(AF_INET, SOCK_STREAM)  # socket for clients to connect to this server
server_sock.bind(('0.0.0.0', const.CHAT_SERVER_PORT))
server_sock.listen(5)  # may change if too many clients

print("Chat Server is ready...")


while True:
    try:
        (conn, addr) = server_sock.accept()  # returns new socket and addr. client
        print(conn, addr)
    except KeyboardInterrupt:
        break

server_sock.close()
