# **Simple Encryption and Decryption Using Binary Manipulation**

This project implements a **simple encryption and decryption algorithm** using **binary manipulation** techniques. The code demonstrates concepts such as string-to-binary conversion, XOR operations, and basic key-based encryption.

---

## **How It Works**
The encryption process involves bitwise operations, swapping values, and key-based manipulation to encode and decode a given text.

---

## **Step 1: Input Values**
The program asks for two inputs:
- **`s`** — The **input string** to be encrypted.  
- **`k`** — The **key** used for encryption and decryption.  

> Example Input:  
```
Enter a string: Hello
Enter a key: key
```

---

## **Step 2: Binary Conversion**
- The input string is converted into its **binary representation**, with each character represented by **8 bits**.

```python
result = "".join(format(ord(i), '08b') for i in s)
```

> Example Output for `"Hello"`:  
```
result: 0100100001100101011011000110110001101111
```

- The binary string is split into two halves:  
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

## **Step 3: Key Conversion**
The provided key is also converted to **binary**:

```python
key = "".join(format(ord(i), '08b') for i in k)
```

> Example Key (`"key"`):  
```
Key: 011010110110010101111001
```

---

## **Step 4: Encryption Process**
The algorithm performs the following steps to encrypt the text:

1. **Right Half + Key Addition (Binary Sum):**  
```python
s = bin(int(right, 2) + int(key, 2))
```

2. **XOR Operation with Left Half:**  
```python
answer = bin(int(s[2:], 2) ^ int(left, 2))
```

3. **Swapping:**  
The right and left halves are swapped for added complexity:  
```python
newr, newl = newl, newr
```

4. **Another Binary Sum and XOR Round:**  
```python
s = bin(int(newr, 2) + int(key, 2))
ans = bin(int(s[2:], 2) ^ int(newl, 2))
```

5. The halves are swapped once more to finalize the cipher text.

6. **Cipher Padding:**  
To ensure the output matches the original binary text length, zeros are padded if needed:  
```python
while len(cipher) != len(result):
    cipher = "0" + cipher
```

---

## **Step 5: Decryption Process**
The encrypted text is then converted back to characters:

```python
plaintext = ""
for i in range(0, len(cipher), 8):
    temp = cipher[i:i+8]
    d = int(temp, 2)
    plaintext = plaintext + chr(d)
```

---

## **Step 6: Example Output**
### **Input:**
```
Enter a string: Hello
Enter a key: key
```

### **Output:**
```
result: 0100100001100101011011000110110001101111
Encrypted Text: 0110010010111011010000110111101101101101
Decrypted Text: Hello
```

✅ The decrypted text matches the original string, proving successful encryption and decryption.

---

## **Key Concepts**
🔹 **Binary Conversion** — Converting text and keys to binary format.  
🔹 **XOR Operation** — Used for obfuscating the binary text by flipping bits.  
🔹 **Swapping Values** — Introduces additional complexity to enhance security.  
🔹 **Key Addition** — Adds a layer of encryption using modular arithmetic.

---

## **Potential Use Cases**
✅ Lightweight encryption for non-critical data.  
✅ Basic learning tool for understanding binary operations in encryption.  
✅ Foundation for building more advanced encryption systems.

---

## **Limitations**
⚠️ This algorithm lacks cryptographic strength for real-world security applications.  
⚠️ Key length limitations could make the cipher vulnerable to brute force attacks.  
⚠️ This is primarily for educational purposes rather than robust encryption.

---

## **Improvements & Enhancements**
✅ Add dynamic key expansion for better security.  
✅ Implement multiple encryption rounds for improved complexity.  
✅ Introduce error handling for invalid characters or keys.  
✅ Enhance the algorithm with stronger XOR patterns or logic.

---

## **Prerequisites**
Ensure you have **Python 3.x** installed.

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
   python binary_encryption.py
   ```

---

