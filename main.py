import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import os
from encryption_tool import generate_key, encrypt_file, decrypt_file

# Generating encryption key
if not os.path.exists("key.key"):
    generate_key()

selected_file = None
def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        selected_file = file_path
        file_label.config(text=file_path)
        show_image_popup(file_path, title="Original Image Preview")

def show_image_popup(image_path, title="Image Preview"):
    try:
        popup = Toplevel()
        popup.title(title)

        img = Image.open(image_path)
        img.thumbnail((500, 500))  # Resize for preview
        img_tk = ImageTk.PhotoImage(img)

        label = tk.Label(popup, image=img_tk)
        label.image = img_tk
        label.pack(padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to preview image: {e}")

def preview_encrypted_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read(512)
            hex_data = content.hex()
            formatted = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))

        popup = Toplevel()
        popup.title("Encrypted Data Preview")

        text = tk.Text(popup, wrap=tk.WORD, width=80, height=20)
        text.insert(tk.END, formatted)
        text.config(state=tk.DISABLED)
        text.pack(padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to preview encrypted data: {e}")

def encrypt_image():
    if not selected_file or not os.path.exists(selected_file):
        messagebox.showerror("Error", "Please select a valid image file.")
        return
    try:
        encrypt_file(selected_file)
        messagebox.showinfo("Success", "Image encrypted successfully!")
        preview_encrypted_data(selected_file)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_image():
    if not selected_file or not os.path.exists(selected_file):
        messagebox.showerror("Error", "Please select a valid image file.")
        return
    try:
        decrypt_file(selected_file)
        messagebox.showinfo("Success", "Image decrypted successfully!")
        show_image_popup(selected_file, title="Decrypted Image Preview")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("🛡️ Image Encryption Tool")
root.geometry("400x250")
root.resizable(True, True)
root.minsize(400, 250)

title_label = tk.Label(root, text="🛡️ Image Encryption Tool", font=("Helvetica", 16, "bold"))
title_label.pack(pady=15)

file_label = tk.Label(root, text="No file selected", wraplength=300, fg="gray")
file_label.pack()

browse_btn = tk.Button(root, text="Browse Image", command=select_file, width=20)
browse_btn.pack(pady=10)

encrypt_btn = tk.Button(root, text="Encrypt Image", command=encrypt_image, bg="orange", fg="white", width=20)
encrypt_btn.pack(pady=5)

decrypt_btn = tk.Button(root, text="Decrypt Image", command=decrypt_image, bg="green", fg="white", width=20)
decrypt_btn.pack(pady=5)

root.mainloop()
