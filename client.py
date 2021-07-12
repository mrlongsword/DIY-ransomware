import socket
IP = "10.0.2.7" #server ip
PORT = 1337
data = "IT WORKS"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP,PORT))
    print("Connected to",IP,"at port",PORT)
    s.send(data.encode("utf-8"))
    print("Finished transmitting data!")
    s.close()
