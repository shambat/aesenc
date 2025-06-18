# 🔐 AES Encryption/Decryption Web App

This is a simple Python-based web application that allows users to perform **AES encryption and decryption** directly from their browser. The server is powered by Python's `http.server`, and encryption is handled using the `pycryptodome` library. The frontend is styled using TailwindCSS for a modern and responsive UI.

---

## 🚀 Features

- 🔒 **AES Encryption (CBC Mode)**
- 🔓 **AES Decryption**
- 🎨 Beautiful, responsive frontend with TailwindCSS
- 📦 Base64 encoding of ciphertext
- 🧪 Ideal for cryptography demonstrations, CTF challenges, or red team simulations

---

## 📁 Project Structure

```plaintext
.
├── server.py           # Main Python script running the HTTP server
└── README.md           # Project documentation
```

---

## 🧰 Requirements

- Python 3.x
- [pycryptodome](https://pypi.org/project/pycryptodome/)

Install dependencies:

```bash
pip install pycryptodome
```

---

## 💻 Usage

### 🔧 Start the Server

```bash
python server.py
```

The server will run on [http://localhost:8000](http://localhost:8000)

---

## 🧪 How to Use

1. Enter the **text** you want to encrypt or decrypt.
2. Provide a **key** (minimum 16 characters recommended).
3. Click **Encrypt** or **Decrypt**.
4. View the result in the output box.

> ✅ Uses AES with **CBC mode** and automatic PKCS7 padding.

---

## 🔐 AES Key Handling

- Accepts keys of any length and pads them to 16/24/32 bytes.
- If the key is longer than 32 bytes, it will be truncated.
- Always use a **secure, random key** in production.

---

## 📷 Screenshot

![Screenshot of AES Web App](https://via.placeholder.com/800x400.png?text=AES+Encryption+Web+App)

---

## 🔍 Security Note

This tool is designed for educational or internal testing purposes. **Do not use it to handle real sensitive data in production environments.**

---

## 📦 Deployment Ideas

- Run as a secure internal tool for your SOC team.
- Deploy on a local VM for classroom or workshop use.
- Integrate with other tools like **Hashcat** for encrypted data analysis.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙋‍♂️ Author

**Muhammad Ehtisham**  
Cyber Security Enthusiast | SOC Analyst | Python Developer  
[LinkedIn](https://www.linkedin.com/in/ehtishamcyber) • [Email](mailto:CONNECTSHAM95@GMAIL.COM)

> "ChatGPT saves the day! Passwords strong enough to make hackers hard time bruteforcing."
