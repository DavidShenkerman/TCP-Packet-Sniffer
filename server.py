import socket
import time

HEADERSIZE = 10
#creates Ipv4, TCP socket binded to local address on port 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4000))
#starts listening for connections
s.listen(5)

while True:
     clientsocket, address = s.accept()
     print(f"Connection from {address} established")

     msg = "Welcome to the server!"
     msg = f'{len(msg):<{HEADERSIZE}}' + msg

     clientsocket.send(bytes(msg, "utf-8"))
     while True:
          time.sleep(3)
          msg = f"The time is! {time.time()}"
          msg = f'{len(msg):< {HEADERSIZE}}'+ msg
          clientsocket.send(bytes(msg, "utf-8"))