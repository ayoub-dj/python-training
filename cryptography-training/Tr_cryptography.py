import string, random

chars = list(string.printable)
key = chars.copy()
random.shuffle(key)

plain_text = 'Hello World'

encrypted_text_c = ''.join(key[chars.index(i)] for i in plain_text)
decrypted_text_c = ''.join(chars[key.index(i)] for i in encrypted_text_c)

import onetimepad
encrypted_text_onetimepad = onetimepad.encrypt(plain_text, 'random')
decrypted_text_onetimepad = onetimepad.decrypt(encrypted_text_onetimepad, 'random')


# Symmetric cryptography uses the same key for both encryption and decryption
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_text_f = cipher.encrypt(plain_text.encode())
decrypted_text_f = cipher.decrypt(encrypted_text_f)


# asymmetric cryptography uses a pair of keys — public and private.
import rsa
from pathlib import Path

def encrypt_file():
    file_path = str(input('Type the path of the file that you wanna encrypt: '))
    file = Path(rf"{file_path}")
    public_key, private_key = rsa.newkeys(605)
    if file.exists():
        file_content = file.read_bytes()
        encrypted_file_rsa = rsa.encrypt(file_content, public_key)

        with open('encrypted_file_rsa.txt', 'wb') as f: f.write(encrypted_file_rsa)

        with open("private_key.key", "wb") as k: k.write(private_key.save_pkcs1())

        return ("""
        We have successfully encrypted your file. In new file called [ encrypted file_rsa.text ] 

        You can use your private key to decrypt the file
        Don't share it with anyone
        In new file called [ private_key.key] 
        """)

    else: return 'Wrong Path'


def decrypt_file():
    with open(rf'encrypted_file_rsa.txt', 'rb') as f: encrypted_text = f.read()
    with open(rf'private_key.key', 'rb') as k: private_key = rsa.PrivateKey.load_pkcs1(k.read())

    return rsa.decrypt(encrypted_text, private_key).decode()
