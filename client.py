import socket

HEADERSIZE = 10

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect((socket.gethostname(), 4000))
while True:
    ful_msg = ''
    new_msg = True
    while True:
        msg = cs.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
        ful_msg += msg.decode("utf-8")
        if len(ful_msg) - HEADERSIZE == msg_len:
            print("full message received")
            print(ful_msg[HEADERSIZE:])
            new_msg = True
            ful_msg = ''