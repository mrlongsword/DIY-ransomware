# DIY-ransomware
<p>An attempt at creating ransomware(for research purposes only).<p>
<p>DO NOT run the pre-built executables in the 'binaries' folder.</p>

## Video demo
<a href="https://youtu.be/VED0ZYSS3_s">https://youtu.be/VED0ZYSS3_s</a>
## Usage
### Build the encryptor using pyinstaller
```
pyinstaller --onefile -w encryptor.py keygen.py
# The generated executable can be found in the 'dist' folder.
```
### On the attacker machine, start the server
<img width="246" alt="image" src="https://user-images.githubusercontent.com/60816759/170675860-d7e666a0-26aa-4420-9b3d-bd8b28b4dfe4.png">

### On the victim machine, execute 'encryptor.exe'
<img width="390" alt="image" src="https://user-images.githubusercontent.com/60816759/170677418-7e19742e-d734-4d3e-8005-129e75ba53c1.png">

### Looking at our server, we see we've received the key from the victim
<img width="398" alt="image" src="https://user-images.githubusercontent.com/60816759/170678184-38e473e5-cd91-4952-857b-3c42af3170fb.png">


