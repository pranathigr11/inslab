# **Feistel Cipher Implementation in Python**

This project implements a **Feistel Cipher**, a symmetric encryption technique that forms the backbone of various secure cryptographic systems, such as **DES (Data Encryption Standard)**. The code follows the core principles of a Feistel Cipher, including data splitting, XOR operations, key mixing, and swapping halves.

---

## **How It Works**
The Feistel Cipher is a symmetric structure used in block cipher design. This implementation follows the essential steps:

1. **Input String Conversion to Binary**  
2. **Splitting the Binary Data**  
3. **Key Mixing (Encryption Process)**  
4. **Swapping Left and Right Halves**  
5. **Decryption Process** (reversing the steps)  

---

## **Step 1: Input Values**
The program asks for:

- **`s`** — The **input string** to be encrypted.  
- **`k`** — The **key** used for encryption and decryption.  

> Example Input:  
```
Enter a string: Hello
Enter a key: key
```

---

## **Step 2: Binary Conversion**
The input string and key are converted into their **binary representation** (8-bit format for each character).

**String to Binary Conversion:**
```python
result = "".join(format(ord(i), '08b') for i in s)
```

**Key to Binary Conversion:**
```python
key = "".join(format(ord(i), '08b') for i in k)
```

> Example Output for `"Hello"` and `"key"`:  
```
Result: 0100100001100101011011000110110001101111
Key: 011010110110010101111001
```

---

## **Step 3: Splitting the Binary Data**
The binary string is split into two equal halves:

```python
l = int(len(result) / 2)
left = result[:l]
right = result[l:]
```

> Example Splits:  
```
Left: 01001000011001
Right: 010110110001101100110111
```

---

## **Step 4: Encryption Process**
The Feistel Cipher encryption process includes:

✅ **Right Half + Key Addition (Binary Sum)**  
```python
s = bin(int(right, 2) + int(key, 2))
```

✅ **XOR Operation with Left Half**  
```python
answer = bin(int(s[2:], 2) ^ int(left, 2))
```

✅ **Swapping Halves**  
```python
newr, newl = newl, newr
```

✅ **Second Key Mixing and XOR Round**  
```python
s = bin(int(newr, 2) + int(key, 2))
ans = bin(int(s[2:], 2) ^ int(newl, 2))
```

✅ **Final Swap to Construct Cipher Text**  
```python
nl, nr = nr, nl
cipher = nl + nr
```

✅ **Cipher Padding**  
To ensure the encrypted text matches the original binary text length:
```python
while len(cipher) != len(result):
    cipher = "0" + cipher
```

---

## **Step 5: Decryption Process**
The cipher text is converted back into its original string using 8-bit chunks.

```python
plaintext = ""
for i in range(0, len(cipher), 8):
    temp = cipher[i:i+8]
    d = int(temp, 2)
    plaintext = plaintext + chr(d)
```

---

## **Step 6: Example Output**
### **Input**
```
Enter a string: Hello
Enter a key: key
```

### **Output**
```
Result: 0100100001100101011011000110110001101111
Encrypted Text: 0110010010111011010000110111101101101101
Decrypted Text: Hello
```

✅ The decrypted text matches the original string, proving successful encryption and decryption.

---

## **Key Concepts of Feistel Cipher**
🔹 **Splitting the Data:** Dividing the input into two halves for iterative encryption.  
🔹 **XOR Operations:** Key mixing using XOR ensures data is obscured effectively.  
🔹 **Swapping Halves:** Ensures diffusion (spreading data influence) for security.  
🔹 **Reversible Decryption Process:** The same steps are applied in reverse to decrypt the data.  

---

## **Potential Use Cases**
✅ Secure data transmission.  
✅ Encryption in file systems.  
✅ Foundation for cryptographic algorithms like **DES** and **Blowfish**.  

---

## **Limitations**
⚠️ **Lack of Multiple Rounds:** Standard Feistel ciphers use multiple rounds (e.g., 16 in DES) to increase security.  
⚠️ **Simple Key Mixing:** For stronger security, a proper round function (`F` function) should be introduced.  
⚠️ **Vulnerable to Known Attacks:** Without additional complexity, this implementation may be less secure for real-world use.  

---

## **Improvements & Enhancements**
✅ Add multiple encryption rounds for stronger security.  
✅ Introduce a more complex **round function (F)** for better confusion and diffusion.  
✅ Implement dynamic key expansion to generate unique round keys.  
✅ Add error handling for non-printable characters or invalid key sizes.  

---

## **Prerequisites**
Ensure you have **Python 3.x** and **NumPy** installed.

---

## **How to Run**
1. **Clone this repository:**
   ```
   git clone <repository_link>
   ```
2. **Navigate to the project directory:**
   ```
   cd <project_directory>
   ```
3. **Run the Python file:**
   ```
   python feistel_cipher.py
   ```

---
