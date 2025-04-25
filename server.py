'''
🔐 Τι κάνει αυτό το σύστημα;
1. Δημιουργία κλειδιού και κρυπτογράφηση
  -Client: Δημιουργεί ένα τυχαίο κλειδί AES 128-bit (16 bytes) για την κρυπτογράφηση των δεδομένων.
  -Κρυπτογραφεί αυτό το AES κλειδί με το δημόσιο κλειδί RSA του server, ώστε να μεταφερθεί με ασφάλεια.

2. Αποστολή του κλειδιού
  -Client: Στέλνει το κρυπτογραφημένο AES κλειδί στον server μέσω του socket.
  -Server: Παραλαμβάνει το κρυπτογραφημένο AES κλειδί και το αποκρυπτογραφεί με το ιδιωτικό RSA κλειδί του, ώστε να ανακτήσει το αρχικό AES κλειδί.

3. Κρυπτογραφημένη επικοινωνία
  -Client: Κρυπτογραφεί όλα τα επόμενα μηνύματα με το AES κλειδί (σε CBC mode) πριν τα στείλει στον server.
  -Server: Παραλαμβάνει τα κρυπτογραφημένα μηνύματα, τα αποκρυπτογραφεί με το ίδιο AES κλειδί και βλέπει τα αρχικά μηνύματα.

🔄 Πώς λειτουργεί συνοπτικά:
    1. Ο client συνδέεται στον server.
    2. Στέλνει το κρυπτογραφημένο AES κλειδί.
    3. Ο server αποκρυπτογραφεί το κλειδί και το αποθηκεύει.
    4. Από εκεί και πέρα, όλη η επικοινωνία (εντολές, μηνύματα) είναι κρυπτογραφημένη με το AES κλειδί και δεν μπορεί να διαβαστεί χωρίς αυτό.

🛡️ Γιατί είναι ασφαλές και stealth:
  -AES-CBC mode: Παρέχει συμμετρική κρυπτογράφηση που είναι γρήγορη και ασφαλής.
  -RSA για key exchange: Εξασφαλίζει ότι το AES κλειδί μεταφέρεται με ασφάλεια.
  -Pure Python AES χωρίς εξωτερικά imports: Μειώνει την πιθανότητα ανίχνευσης από
   antivirus, αφού δεν χρησιμοποιούνται κλασικές βιβλιοθήκες που μπορεί να ανιχνευτούν εύκολα.
--------------------------------------------------------------------------------------------------------------------------
🔐 What this system does:
1. Key generation and encryption
-Client: Creates a random AES 128-bit key (16 bytes) to encrypt the data.
-It encrypts this AES key using the server's RSA public key so it can be transferred securely.

2. Sending the key
-Client: Sends the encrypted AES key to the server over the socket connection.
-Server: Receives the encrypted AES key and decrypts it using its RSA private key to recover the original AES key.

3. Encrypted communication
-Client: Encrypts all further messages with the AES key (in CBC mode) before sending them.
-Server: Receives the encrypted messages, decrypts them using the same AES key, and reads the original plaintext.

🔄 How it works, step-by-step:
1. The client connects to the server.
2. It sends the RSA-encrypted AES key.
3. The server decrypts and stores the AES key.
4. From that moment on, all communication (commands, messages) is AES-encrypted and unreadable without the key.

🛡️ Why it is secure and stealthy:
-AES-CBC mode: Provides fast, symmetric encryption that is industry-standard secure.
-RSA for key exchange: Ensures the AES key is safely transferred over the network.
-Pure Python AES with no external imports: Reduces the chance
 of antivirus detection because there are no obvious Crypto library imports.

 How to run:
 1. python RSAkeys.py # make key private.pem for server and public.pem for client
 2. python server.py
 3. python client.py

 C:\Python311\python.exe C:\Users\dev\Documents\PythonProject\chat_AES_encryption\AES_PURE\server.py
[*] Listening on port 4444...
[+] Connection from ('127.0.0.1', 65280)
[CLIENT]: dir C:\\
'''

import socket
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pure_aes_cbc import PureAESCipher

# Load server's private key
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())
rsa_cipher = PKCS1_OAEP.new(private_key)

# Start server
s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)
print("[*] Listening on port 4444...")

conn, addr = s.accept()
print(f"[+] Connection from {addr}")

# Receive and decrypt AES key
encrypted_key = conn.recv(256)
aes_key = rsa_cipher.decrypt(encrypted_key)
aes_cipher = PureAESCipher(aes_key)

# Receive encrypted message
encrypted_data = conn.recv(4096)
decrypted_message = aes_cipher.decrypt(encrypted_data.decode())
print("[CLIENT]:", decrypted_message)

conn.close()
s.close()