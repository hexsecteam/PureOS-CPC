# PureOS-CPC: Stealth Encrypted Communication Engine

## Overview

PureOS-CPC (Pure Obfuscated Secure Communication Protocol) is a lightweight, pure Python implementation designed to establish encrypted communication between a client and a server. It uses a stealthy AES-128 encryption algorithm combined with RSA for secure key exchange, all without relying on external cryptographic libraries.
Built with cybersecurity research in mind by the HexSec team, PureOS-CPC ensures that data transmitted over the network remains confidential, tamper-proof, and extremely hard to detect by traditional antivirus and endpoint protection systems.
---

## How It Works

- **AES Key Generation:**
  - Each client session begins by generating a new random AES-128 (16 bytes) symmetric encryption key.

- **RSA Key Exchange:**
  - The AES key is encrypted using the server's RSA public key.
  - The encrypted AES key is sent to the server, ensuring that no plaintext key is ever exposed over the network.

- **Encrypted Communication:**
  - Once the server decrypts the AES key with its private RSA key, all further communication is AES-encrypted in CBC (Cipher Block Chaining) mode.
  - Messages are padded and encrypted before transmission and securely decrypted on reception.

- **Stealth Features:**
  - No external libraries like `pycryptodome` are imported, reducing the risk of static detection by antivirus software.
  - The AES-CBC engine is fully written in pure Python and obfuscated to blend into benign software behavior.

---

## Purpose and Research Context

PureOS-CPC is intended as a research-grade framework to study:
- Stealthy encrypted communication between remote systems.
- Evasion techniques against static and behavioral malware detection.
- Development of secure, minimalistic communication protocols for remote administration, pentesting, and cybersecurity simulations.

**At runtime**, the client performs legitimate-looking operations, initiating a key exchange handshake, and proceeding with encrypted messaging. Due to the nature of pure Python code and obfuscation, detection by standard antivirus engines becomes significantly more difficult compared to common tools using well-known cryptographic libraries.

---

## Key Features

- 🔐 Fully Encrypted Communication (AES-128-CBC)
- 🛡️ Secure RSA Key Exchange (2048-bit recommended)
- ✨ Pure Python Implementation (No external Crypto libraries)
- 📢 Hard to detect by signature-based antivirus systems
- ✨ Lightweight and easy to integrate

---

## How to Run

1. Generate RSA keys for the server and client:
   ```bash
   python RSAkeys.py
   ```
   This will create `private.pem` for the server and `public.pem` for the client.

2. Start the server:
   ```bash
   python server.py
   ```

3. Start the client:
   ```bash
   python client.py
   ```
   
   Example output:
   ```
   C:\\Python311\\python.exe C:\\Users\\dev\\Documents\\PythonProject\\chat_AES_encryption\\AES_PURE\\server.py
   [*] Listening on port 4444...
   [+] Connection from ('127.0.0.1', 65280)
   [CLIENT]: dir C:\\\
   ```

---

## Support the HexSec Community

If you find value in our work and would like to support the HexSec community, you can contribute by making a donation. Your support helps us continue developing innovative and high-quality tools for the cybersecurity and IT community.

**Donate:**
- **ETH:** `0x3E79B73e3ce33c6B860425DCB40c6D2f4F2aC508`
- **BTC:** `bc1qpex9u7x4a6kj4nf6fee7mz54vsv4th2rj2pt30`

**For more details:**
- **Contact on Telegram:** [@Hexsecteam](https://t.me/Hexsecteam)
- **Group on Telegram:** [@hexsec_tools](https://t.me/hexsec_tools)

✩ Cybersecurity | Secure Development | Ethical Research | Security Engineering

---

## Disclaimer

**This tool is intended for legitimate and ethical use by IT professionals and system administrators.**

Any misuse for unauthorized access, malicious purposes, or violation of laws and regulations is strictly prohibited. Use PureOS-CPC responsibly and only in compliance with all applicable local, national, and international laws.

