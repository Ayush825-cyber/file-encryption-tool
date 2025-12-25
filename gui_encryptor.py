import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# ---------------- LOAD KEY ----------------
def load_key():
    if not os.path.exists("secret.key"):
        messagebox.showerror("Error", "secret.key not found. Generate key first.")
        return None
    return open("secret.key", "rb").read()

# ---------------- ENCRYPT FILE ----------------
def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    key = load_key()
    if key is None:
        return

    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "wb") as file:
        file.write(encrypted)

    messagebox.showinfo("Success", "File encrypted successfully!")

# ---------------- DECRYPT FILE ----------------
def decrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    key = load_key()
    if key is None:
        return

    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted = fernet.decrypt(encrypted_data)
    except:
        messagebox.showerror("Error", "Invalid key or corrupted file")
        return

    original_file = file_path.replace(".enc", "")
    with open(original_file, "wb") as file:
        file.write(decrypted)

    messagebox.showinfo("Success", "File decrypted successfully!")

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("File Encryption Tool")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="File Encryption Tool", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Encrypt File", width=20, command=encrypt_file).pack(pady=5)
tk.Button(root, text="Decrypt File", width=20, command=decrypt_file).pack(pady=5)

tk.Label(root, text="AES-based Secure Encryption", font=("Arial", 9)).pack(pady=10)

root.mainloop()
