# **Vigenère Cipher in Python**  

## **Overview**  
This Python script implements the **Vigenère Cipher**, a method of encrypting and decrypting text using a keyword-based shift. The Vigenère Cipher is a polyalphabetic substitution cipher that enhances security over simple Caesar ciphers.  

## **Features**  
✅ Encrypts a given plaintext using the **Vigenère Cipher** algorithm.  
✅ Decrypts the ciphertext back to the original plaintext.  
✅ Automatically **converts all input to uppercase** for consistency.  
✅ Supports **non-alphabetic characters**, which remain unchanged.  
✅ Uses a **repeating keyword** to determine the shifting pattern.  

## **How to Run the Code**  

### **1. Prerequisites**  
Ensure you have **Python 3.x** installed on your system. Download it from the official Python website:  
[Download Python](https://www.python.org/downloads/)  

### **2. Clone the Repository**  
Clone this repository to your local machine using the following command:  
```bash
git clone https://github.com/pranathigr11/inslab.git
```

### **3. Navigate to the Project Folder**  
After cloning, navigate to the folder where the project is located:  
```bash
cd Vigenere_Cipher
```

### **4. Run the Code**  
To run the Vigenère Cipher script, use:  
```bash
python vigenere_cipher.py
```

---

## **How It Works**  

### **Encryption Process**  
- The **plaintext** and **key** are converted to uppercase.  
- Each letter in the plaintext is shifted forward based on the corresponding letter in the key.  
- The shift value is determined by the **position of the key letter** in the alphabet (A = 0, B = 1, ..., Z = 25).  
- The key repeats to match the length of the plaintext.  
- Non-alphabetic characters remain unchanged.  

### **Decryption Process**  
- The **ciphertext** and **key** are converted to uppercase.  
- Each letter in the ciphertext is shifted backward based on the corresponding letter in the key.  
- The shift value is determined by the **position of the key letter** in the alphabet.  
- The key repeats to match the length of the ciphertext.  
- Non-alphabetic characters remain unchanged.  

---

## **Example Execution**  

### **Input:**  
```bash
Enter plaintext: HELLO  
Enter key: KEY  
```

### **Encryption Output:**  
```bash
Encrypted: RIJVS  
```

### **Decryption Output:**  
```bash
Decrypted: HELLO  
```

---

## **Code Explanation**  

### **Functions**  
1. **`vigenere_encrypt(plaintext, key)`**  
   - Converts plaintext and key to uppercase.  
   - Encrypts each letter using the key’s corresponding shift.  
   - Returns the encrypted ciphertext.  

2. **`vigenere_decrypt(ciphertext, key)`**  
   - Converts ciphertext and key to uppercase.  
   - Decrypts each letter using the key’s corresponding shift.  
   - Returns the decrypted plaintext.  

---

## **Customization**  
- Modify the `key` to experiment with different encryption results.  
- Extend the script to handle **lowercase letters** without converting everything to uppercase.  
- Implement **automatic key generation** based on user-defined security rules.  

---

## **Requirements**  
- **Python 3.x** (No additional libraries required)  

---

## **Additional Information**  
The **Vigenère Cipher** is significantly more secure than the **Caesar Cipher** because it avoids simple frequency analysis. However, it is still vulnerable to **Kasiski examination** and **frequency-based cryptanalysis**.  

For stronger encryption, consider using **modern cryptographic algorithms** like **AES (Advanced Encryption Standard)**.  

---

