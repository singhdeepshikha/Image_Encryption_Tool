

---

```markdown
# 🛡️Image Encryption Tool

A secure and beginner-friendly desktop GUI application to encrypt and decrypt image files using symmetric encryption (Fernet). Built with Python, Tkinter, and Cryptography, this tool helps protect sensitive visual data from unauthorized access or tampering.

---
```
## ✨ Features

- 🔐 Encrypts image files (`.png`, `.jpg`, `.jpeg`, `.bmp`)
- 🔓 Decrypts and restores images to original form
- 🧾 Live **hexadecimal preview** of encrypted binary data
- 🖼️ Visual **before and after** previews (image popups)
- ⚙️ Clean and intuitive **Tkinter GUI**
- 🔑 Auto-generates and stores a symmetric encryption key
- ✅ Safe for cloud backup and secure sharing

---

## 🔐 How It Works

- Uses **Fernet** (AES 128-bit encryption with HMAC)
- Saves a unique encryption key to `key.key`
- Encrypted images appear scrambled and unreadable
- Images can only be decrypted with the correct key
- Ensures **confidentiality**, **integrity**, and **security**

---

## 📁 Project Structure

```
image-encryption-tool/
├── encryption_tool.py     # Encryption/decryption functions
├── main.py                # Tkinter GUI and user actions
├── key.key                # Auto-generated symmetric key (Fernet)
├── sample_images/         # (Optional) Folder for testing
└── README.md              # Project documentation
```

---

## 🛠️ Requirements

Make sure Python 3.8 or later is installed.

Install the required packages:

```bash
pip install cryptography pillow
```

---

## ▶️ Usage

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
```

2. **Run the application**:

```bash
python main.py
```

3. **Steps**:
   - Click **Browse Image** to select an image
   - Click **Encrypt** to securely scramble it (hex preview shown)
   - Click **Decrypt** to restore it (visual preview shown)

---

## 🔍 Preview Snapshots

| Action           | Output        |
|------------------|---------------|
| Select Image     | Image popup   |
| Encrypt Image    | Hex data popup |
| Decrypt Image    | Image restored popup |

---

## 📌 Use Cases

- 🔒 Securing personal or sensitive photos
- 🧾 Protecting scanned IDs, certificates, or documents
- ☁️ Encrypting files before uploading to cloud storage
- 🛡️ Visual privacy protection for data sharing
- 📚 Educational tool for learning image encryption

---

## 🚀 Future Improvements

- 🔑 Password-based key derivation (PBKDF2)
- 🗂️ Batch folder encryption
- 🖱️ Drag-and-drop support
- 🎨 Dark mode & themes
- 🧾 Export action log or history
- 💻 Build into `.exe` for Windows desktop use

