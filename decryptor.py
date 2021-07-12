import pyAesCrypt
import os
import sys
cwd = os.getcwd()

key = input("Enter the key:")
for root,dirs,files in os.walk(cwd):
    for file in files:
        
        encrypted = (root+"\\"+file)
        file_path,file_ext = os.path.splitext(root+"\\"+file)
        decrypted = file_path
        
        if file_ext == ".foobar":
            try:
                print("Attempting to decrypt",str(encrypted))
                pyAesCrypt.decryptFile(encrypted, decrypted, key)
                print("Decrypting",str(encrypted))
                os.remove(encrypted)
            except:
                print("Error!Invalid key.")
