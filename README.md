# DIY-ransomware
<p>An attempt at creating ransomware(for research purposes only).<p>
<p>DO NOT run the pre-built executables in the 'binaries' folder.</p>

## Video demo
<a href="https://youtu.be/VED0ZYSS3_s">https://youtu.be/VED0ZYSS3_s</a>
## Usage
### Build the encryptor using pyinstaller
```
pyinstaller --onefile -w encrypt.py keygen.py
```
### On the attacker machine, start the server
<img width="246" alt="image" src="https://user-images.githubusercontent.com/60816759/170675860-d7e666a0-26aa-4420-9b3d-bd8b28b4dfe4.png">
### On the victim machine, execute 'encryptor.exe'

