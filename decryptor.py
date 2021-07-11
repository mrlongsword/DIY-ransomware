import pyAesCrypt
import os
import sys
cwd = os.getcwd()
#print(cwd)
key = "password"
for root,dirs,files in os.walk(cwd):
    for file in files:
        #print(root+"\\"+file)
        encrypted = (root+"\\"+file)
        file_path,file_ext = os.path.splitext(root+"\\"+file)
        decrypted = file_path
        #print(file_ext)
        if file_ext == ".foobar":
            #print(encrypted)
            pyAesCrypt.decryptFile(encrypted, decrypted, key)
            os.remove(encrypted)
        
                
#print(sys.argv[0])
