# File Encryption Tool (Python)

## Description
A Python-based file encryption and decryption tool using AES symmetric encryption.
It allows users to securely protect files using a secret key.

## Features
- Encrypt any file type
- Secure AES-based encryption
- Decrypt files safely
- Command-line interface

## Requirements
- Python 3.x
- cryptography library

## Usage

### Generate key
python file_encryptor.py --genkey

### Encrypt file
python file_encryptor.py --encrypt filename

### Decrypt file
python file_encryptor.py --decrypt filename.enc

## Note
Keep the secret.key file safe. Losing it means losing access to encrypted data.
