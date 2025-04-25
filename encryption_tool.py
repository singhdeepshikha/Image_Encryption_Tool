from cryptography.fernet import Fernet
import os

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("key.key", "rb").read()

# Encrypt an image
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Decrypt an image
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as dec_file:
        dec_file.write(decrypted)
