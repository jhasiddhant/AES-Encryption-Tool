from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import encryption
import decryption

print("==================================")
print("Encryption and Decryption of Files")
print("==================================")
print("[1] Encryption")
print("[2] Decryption")
print("[3] Exit")
print("==================================")

while True:
    choice = input('\n->')

    if choice == '1':
        key = input('Enter a key to encrypt the file.\n->')
        key = key.encode('UTF-8')
        key = pad(key, AES.block_size)
        filename = input('Enter the name of the file which is to be encrypted.\n->')
        encryption.encryption(filename, key)
        break
        
    elif choice == '2':
        keyd = input('Enter a key to decrypt the file.\n->')
        keyd = keyd.encode('UTF-8')
        keyd = pad(keyd, AES.block_size)
        filenamed = input('Enter the name of the file which is to be decrypted..\n->')
        decryption.decryption(filenamed ,keyd)
        break
    
    elif choice == '3':
        exit()

    else:
        print('Wrong Choice Entered.... \n[1] Encryption \n[2] Decryption \n[3] Exit->')
