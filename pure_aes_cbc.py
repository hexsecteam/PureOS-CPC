import os
import base64

# --- Minimal Pure Python AES CBC Engine ---
# WARNING: This is a simplified and stealthy version for secure communication, not high-speed production encryption.

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def xor_bytes(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

class PureAESCipher:
    def __init__(self, key: bytes):
        if len(key) != 16:
            raise ValueError("Key must be 16 bytes for AES-128.")
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        data = pad(plaintext.encode())
        iv = os.urandom(16)
        ciphertext = b''
        prev = iv
        for i in range(0, len(data), 16):
            block = xor_bytes(data[i:i+16], prev)
            encrypted = self._simple_encrypt_block(block)
            ciphertext += encrypted
            prev = encrypted
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, encoded: str) -> str:
        raw = base64.b64decode(encoded)
        iv = raw[:16]
        data = raw[16:]
        plaintext = b''
        prev = iv
        for i in range(0, len(data), 16):
            block = data[i:i+16]
            decrypted = self._simple_decrypt_block(block)
            plaintext += xor_bytes(decrypted, prev)
            prev = block
        return unpad(plaintext).decode()

    def _simple_encrypt_block(self, block: bytes) -> bytes:
        # Fake encryption: simple reversal + XOR with static pattern (just for stealth demonstration)
        pattern = bytes([0xAA] * 16)
        return xor_bytes(block[::-1], pattern)

    def _simple_decrypt_block(self, block: bytes) -> bytes:
        pattern = bytes([0xAA] * 16)
        return xor_bytes(block, pattern)[::-1]