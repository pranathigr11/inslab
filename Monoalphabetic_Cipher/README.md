

---

# **Monoalphabetic Substitution Cipher Encryption & Decryption in Python**

## **Overview**
This Python script implements a **Monoalphabetic Substitution Cipher**, where each letter in the plaintext is replaced by a corresponding letter from a custom cipher alphabet. The program allows users to input a text, encrypt it using the monoalphabetic substitution cipher, and decrypt it back to its original form.

## **Features**
- ✅ Encrypts a given text using the **Monoalphabetic Substitution Cipher** algorithm with a custom cipher alphabet.
- ✅ Decrypts the encrypted text back to the original message.
- ✅ Preserves spaces, punctuation, and special characters.
- ✅ Supports both **uppercase and lowercase letters**.

## **How to Run the Code**

### **1. Prerequisites**
Ensure you have **Python 3.x** installed on your system. You can download it from the official Python website:  
[Download Python](https://www.python.org/downloads/)

### **2. Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/pranathigr11/inslab.git
```


### **3. Navigate to the Project Folder**
After cloning, go to the folder where the project is located:
```bash
cd Monoalphabetic_Cipher
```

### **4. Run the Code**
To run the Monoalphabetic Substitution Cipher script:
```bash
python monoalphabetic_cipher.py
```

## **How It Works**
- Each letter in the input text is replaced with a corresponding letter from a custom cipher alphabet (using the predefined `plain` and `cipher` strings).
- Non-alphabetical characters (e.g., spaces, numbers, punctuation) remain unchanged.
- The encryption and decryption processes are reversed using the custom mapping of characters between the `plain` and `cipher` strings.

## **Example Execution**

### **Input:**
```bash
Enter the string of your choice: Hello, World!
```

### **Output:**
```bash
Encrypted text: itssg, vgksr!
Decrypted text: Hello, World!
```

## **Code Explanation**

### **Functions**
1. `encrypt(text)`:
   - Replaces each letter in the input `text` with a corresponding letter from the custom cipher.
   - Converts the text to lowercase for uniformity.
   - Non-alphabetic characters are preserved as they are.

2. `decrypt(text)`:
   - Replaces each letter in the encrypted `text` with a corresponding letter from the `plain` alphabet.
   - Non-alphabetic characters are preserved.

## **Customization**
- Modify the `cipher` string to create your own custom encryption scheme.
- Change the `plain` string if you wish to use a different set of characters for encryption.
- You can also expand the script to handle **uppercase letters** separately or add more characters to the alphabet.

## **Requirements**
- **Python 3.x**

## **Additional Information**
Feel free to modify this script for your own use or to experiment with different encryption techniques. You can also expand the cipher by using more complex substitutions or implementing **polyalphabetic ciphers** like the **Vigenère cipher**.
##**RUNCODE**
https://onlinegdb.com/Quc_VV3re
---

