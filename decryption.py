from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from base64 import b64decode, b64encode, decode

def decryption(file,key):
    with open(file, 'r') as decf:
        try:
            data = decf.read()
            iv = data[:24]
            iv = b64decode(iv)
            ciphertext = data[24:len(data)]
            ciphertext = b64decode(ciphertext)
            cipher = AES.new(key,AES.MODE_CFB,iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted,AES.block_size)
            new_file = input(f'[+] Enter the new file name.\n>')
            with open(new_file, 'wb') as data:
                data.write(decrypted)
            data.close()
            print('Successfully Decrypted....')
            print(f'[!] Note: The decrypted file with name {new_file} will be saved in the current directory')
        except(ValueError,KeyError):
            print('Something Went Wrong..Decryption failed!\nCheck the file type or entered key...')


