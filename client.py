import socket
import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pure_aes_cbc import PureAESCipher

# Load server's public key
with open("public.pem", "rb") as f:
    server_public_key = RSA.import_key(f.read())
rsa_cipher = PKCS1_OAEP.new(server_public_key)

# Generate random AES key
aes_key = os.urandom(16)
aes_cipher = PureAESCipher(aes_key)

# Encrypt AES key with server's public RSA key
encrypted_key = rsa_cipher.encrypt(aes_key)

# Connect to server
s = socket.socket()
s.connect(("127.0.0.1", 4444))
s.sendall(encrypted_key)

# Send encrypted message
message = "dir C:\\\\ ti kaneis"
encrypted_message = aes_cipher.encrypt(message)
s.sendall(encrypted_message.encode())

s.close()