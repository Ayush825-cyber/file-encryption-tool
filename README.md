# File Encryption Tool (Python) 🔐

## Description
A Python-based file encryption and decryption tool using AES symmetric encryption.
It allows users to securely protect files from unauthorized access using a secret key.

---

## Features
- Encrypt any file type (text, image, PDF, etc.)
- Secure AES-based symmetric encryption
- Safe file decryption using the same secret key
- Command-line interface (CLI)
- Graphical user interface (GUI)
- Simple and reliable design

---

## Requirements
- Python 3.x
- cryptography library

Install dependency:
```bash
pip install cryptography
```


## Usage

### Generate key
python file_encryptor.py --genkey

### Encrypt file
python file_encryptor.py --encrypt filename

### Decrypt file
python file_encryptor.py --decrypt filename.enc

### GUI Version
python gui_encryptor.py

## Note
Keep the secret.key file safe. Losing it means losing access to encrypted data.
