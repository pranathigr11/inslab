

# **Caesar Cipher Encryption & Decryption in Python**

## **Overview**
This Python script implements the **Caesar Cipher**, a simple encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. The program allows users to input a text and a shift value to encrypt the message, then decrypts it back to its original form.

## **Features**
- ✅ Encrypts a given text using the **Caesar Cipher** algorithm
- ✅ Decrypts the encrypted text back to the original message
- ✅ Preserves spaces, punctuation, and special characters
- ✅ Supports both **uppercase and lowercase letters**

## **How to Run the Code**

### **1. Prerequisites**
Make sure you have **Python 3.x** installed on your system. You can download it from the official Python website:  
[Download Python](https://www.python.org/downloads/)

### **2. Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/pranathigr11/inslab.git
```


### **3. Navigate to the Project Folder**
After cloning, go to the folder where the project is located:
```bash
cd inslab
```

### **4. Run the Code Locally**
To run the Caesar Cipher script locally:
```bash
python caesar_cipher.py
```

### **5. Run the Code with GitHub Codespaces**  
Alternatively, you can run the code directly on **GitHub Codespaces** without setting up Python locally. This is a cloud-based development environment, and you don't need to install anything on your computer. Just follow these steps:

1. Open this repository on GitHub.
2. Click on the green "Code" button.
3. Select "Open with Codespaces" and then "Create new codespace".
4. Wait for GitHub to set up the environment for you.
5. Once the environment is ready, open the terminal inside Codespaces.
6. Run the following command to execute the code:
   ```bash
   python caesar_cipher.py
   ```

## **How It Works**
- Each letter is shifted forward by the given shift value in encryption.
- Each letter is shifted backward by the same shift value in decryption.
- Non-alphabetical characters (e.g., spaces, numbers, punctuation) remain unchanged.

## **Example Execution**

### **Input:**
```bash
Enter the text: Hello, World!
Enter the shift: 3
```

### **Output:**
```bash
Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

## **Code Explanation**

### **Functions**
1. `caesar_cipher_encryption(text, shift)`:
   - Shifts each letter **forward** by `shift` positions.
   - Maintains case (uppercase/lowercase).
   - Leaves non-alphabetic characters unchanged.

2. `caesar_cipher_decryption(encryption, shift)`:
   - Shifts each letter **backward** by `shift` positions.
   - Maintains case and ignores non-alphabetic characters.

## **Customization**
Feel free to change the **shift** value to any positive or negative integer to adjust the encryption strength. For example:
```python
shift = 5
```
This would shift each letter by 5 positions.

You can also modify the script to handle negative shifts (left shifts) or to implement additional features like randomizing the shift value to enhance security.

## **Requirements**
- **Python 3.x** (if running locally)

## **Additional Information**
If you want to add more functionalities, like handling different cipher techniques, you can modify this script to support other shifts or even add encryption methods like **Vigenère cipher** or **Substitution cipher**.

---

