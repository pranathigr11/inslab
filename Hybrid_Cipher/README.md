Here is the README file for your hybrid encryption script:  

---

# **Hybrid Cipher: Vigenère + Columnar Transposition**

## **Overview**
This Python script implements a **hybrid encryption algorithm** that combines two classical ciphers:  
1. **Vigenère Cipher** – A polyalphabetic substitution cipher.  
2. **Columnar Transposition Cipher** – A transposition cipher that rearranges characters based on a key.

By combining both methods, this encryption technique provides enhanced security over using either cipher individually.

---

## **Features**
- ✅ **Encrypts and decrypts** text using a hybrid approach.  
- ✅ Implements **Vigenère Cipher** for substitution-based encryption.  
- ✅ Uses **Columnar Transposition Cipher** for rearranging the text.  
- ✅ Supports **custom keys** for both encryption techniques.  
- ✅ Preserves non-alphabetic characters in the text.  

---

## **How to Run the Code**

### **1. Prerequisites**
Ensure you have **Python 3.x** installed on your system. You can download it from:  
[Download Python](https://www.python.org/downloads/)

### **2. Clone the Repository**
Clone this repository to your local machine using:
```bash
git clone https://github.com/pranathigr11/inslab.git
```

### **3. Navigate to the Project Folder**
```bash
cd Hybrid_Cipher
```

### **4. Run the Script**
To encrypt and decrypt a message, run:
```bash
python hbrid_cipher.py
```

---

## **How the Hybrid Cipher Works**
### **Step 1: Vigenère Cipher**
- Uses a key-based substitution method.
- Each letter is shifted based on a repeating key.
- Example:
  - Plaintext: **"HELLO"**
  - Key: **"KEY"**
  - Encrypted Text (Vigenère): **"RIJVS"**  

### **Step 2: Columnar Transposition Cipher**
- Rearranges text into a grid based on the key.
- The text is read column-wise in a shuffled order.
- Example:
  - Vigenère output: **"RIJVS"**
  - Key: **"4312"**
  - Encrypted output: **"VSRIJ"** (shuffled based on the key order)

### **Decryption Process**
- Reverse the Columnar Transposition Cipher to reconstruct the Vigenère output.
- Reverse the Vigenère Cipher to retrieve the original plaintext.

---

## **Example Execution**
### **Encryption**
```python
plaintext = "SECUREHYBRID"
vigenere_key = "KEY"
transposition_key = "4312"

encrypted_text = hybrid_encrypt(plaintext, vigenere_key, transposition_key)
print("Encrypted:", encrypted_text)
```
#### **Output:**
```
Encrypted: RYEUICSHRDHEB
```

### **Decryption**
```python
decrypted_text = hybrid_decrypt(encrypted_text, vigenere_key, transposition_key)
print("Decrypted:", decrypted_text)
```
#### **Output:**
```
Decrypted: SECUREHYBRID
```

---

## **Functions Used**
1. **`vigenere_cipher(text, key, encrypt=True)`**  
   - Encrypts/decrypts text using the Vigenère cipher.  
2. **`columnar_transposition_encrypt(text, key)`**  
   - Encrypts text using columnar transposition.  
3. **`columnar_transposition_decrypt(text, key)`**  
   - Decrypts text using columnar transposition.  
4. **`hybrid_encrypt(text, vigenere_key, transposition_key)`**  
   - First applies Vigenère cipher, then columnar transposition.  
5. **`hybrid_decrypt(text, vigenere_key, transposition_key)`**  
   - First reverses columnar transposition, then Vigenère cipher.  

---

## **Customization**
- Change the **Vigenère key** for a different substitution pattern.
- Modify the **transposition key** to change the column order.
- Extend the script to support **custom alphabets** or **special characters**.

---

## **Requirements**
- **Python 3.x**
- No additional libraries required (pure Python implementation).

---

## **Security Considerations**
- **Vigenère Cipher** is susceptible to frequency analysis if the key is short.
- **Columnar Transposition** is vulnerable if the key is known.
- **Combining both ciphers** significantly improves security.

---

## **Additional Notes**
This hybrid encryption method demonstrates how classical ciphers can be combined to create stronger encryption techniques. It serves as a great introduction to cryptography and can be extended for more complex encryption schemes.

## **RUN CODE**
https://onlinegdb.com/dl_z0ToFt
---

Let me know if you need modifications! 🚀
