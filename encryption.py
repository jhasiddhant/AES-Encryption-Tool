from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode


def encryption(file, key):
    with open(file, 'rb') as enc:
        data = enc.read()
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        write = iv + ciphertext
    enc.close()
    with open(file + '.enc', 'w') as data:
        data.write(write)
    data.close()
    print('Successfully Encrypted....')