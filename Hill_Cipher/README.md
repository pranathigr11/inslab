---

# **Hill Cipher Encryption in Python**

## **Overview**
This Python script implements the **Hill Cipher**, a polygraphic substitution cipher that encrypts blocks of letters using matrix multiplication. The Hill Cipher is one of the earliest encryption techniques based on linear algebra and modular arithmetic.

## **Features**
- ✅ Encrypts a given plaintext using the **Hill Cipher** algorithm.
- ✅ Converts all input to **uppercase** and removes spaces.
- ✅ **Automatically pads** the plaintext with "X" if its length is not a multiple of the matrix size.
- ✅ Uses **matrix multiplication** and **modular arithmetic** to transform plaintext into ciphertext.
- ✅ Allows for a **customizable key matrix**.

## **How to Run the Code**

### **1. Prerequisites**
Ensure you have **Python 3.x** installed on your system. You can download it from the official Python website:  
[Download Python](https://www.python.org/downloads/)

Additionally, install the required NumPy library (if not already installed) using:

```bash
pip install numpy
```

### **2. Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/pranathigr11/inslab.git
```

### **3. Navigate to the Project Folder**
After cloning, navigate to the folder where the project is located:
```bash
cd Hill_Cipher
```

### **4. Run the Code**
To run the Hill Cipher encryption script:
```bash
python hill_cipher.py
```

---

## **How It Works**
- **Key Matrix Creation**: A square matrix (e.g., 2x2 or 3x3) is used as the encryption key.
- **Plaintext Processing**:
  - The plaintext is converted to **uppercase** and spaces are removed.
  - If the plaintext length is not a multiple of the key matrix size, **"X"** is appended to complete the required length.
- **Encryption Process**:
  - The plaintext is converted into numerical values (A = 0, B = 1, ..., Z = 25).
  - The plaintext is divided into blocks of size equal to the key matrix dimension.
  - Each block is multiplied by the key matrix, and **mod 26** is applied to keep values within the alphabet range.
  - The resulting numbers are converted back to letters, forming the ciphertext.

---

## **Example Execution**

### **Input:**
```bash
Enter the plaintext: HELLO
```

### **Key Matrix:**
```python
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
```

### **Output:**
```bash
Encrypted: TFJJZX
```

---

## **Code Explanation**

### **Functions**
1. `hill_cipher_encrypt(plaintext, key_matrix)`:
   - Converts the plaintext into numerical values.
   - Ensures the length of the plaintext is a multiple of the matrix size.
   - Splits the plaintext into blocks and encrypts them using **matrix multiplication** and **mod 26**.
   - Converts the result back into letters to form the encrypted text.

---

## **Customization**
- Modify the `key_matrix` to change the encryption.
- Ensure the key matrix is **square (n × n)** and has an **invertible determinant modulo 26** (for decryption).
- To implement **decryption**, compute the **modular inverse** of the key matrix and follow the reverse encryption steps.

---

## **Requirements**
- **Python 3.x**
- **NumPy Library (`pip install numpy`)**

---

## **Additional Information**
The **Hill Cipher** is a strong encryption method but requires a **valid key matrix** (one that has an inverse in **mod 26**) to be decrypted successfully. You can extend this script to include decryption by computing the modular inverse of the key matrix.

---

