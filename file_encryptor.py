from cryptography.fernet import Fernet
import sys
import os
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as secret.key")
def load_key():
    return open("secret.key", "rb").read()
def encrypt_file(filename):
    if not os.path.exists(filename):
        print("[-] File does not exist")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print(f"[+] File encrypted → {filename}.enc")

def decrypt_file(filename):
    if not os.path.exists(filename):
        print("[-] Encrypted file does not exist")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted = fernet.decrypt(encrypted_data)
    except:
        print("[-] Invalid key or corrupted file")
        return

    original_name = filename.replace(".enc", "")
    with open(original_name, "wb") as file:
        file.write(decrypted)

    print(f"[+] File decrypted → {original_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python file_encryptor.py --genkey")
        print("  python file_encryptor.py --encrypt <filename>")
        print("  python file_encryptor.py --decrypt <filename.enc>")
        sys.exit()

    command = sys.argv[1]

    if command == "--genkey":
        generate_key()

    elif command == "--encrypt":
        encrypt_file(sys.argv[2])

    elif command == "--decrypt":
        decrypt_file(sys.argv[2])

    else:
        print("Invalid command")
