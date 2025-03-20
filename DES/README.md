# **DES Key Generator Using Bit Manipulation**

This project implements a **Key Generator for DES (Data Encryption Standard)** using bit manipulation techniques. The code takes a string as input and produces **8 unique keys** that can be used in DES encryption. This project is designed for learning purposes and demonstrates essential concepts such as **binary operations**, **bit shifting**, and **randomization**.

---

## **What is DES?**
**DES (Data Encryption Standard)** is a symmetric-key block cipher that encrypts data in 64-bit blocks. DES uses **16 rounds** of Feistel structure encryption, with each round requiring a **unique 48-bit subkey**. This implementation focuses on generating randomized keys that mimic DES's key generation principles.

---

## **How It Works**
The code follows these steps to generate 8 unique keys:

---

### **Step 1: User Input**
- The user is prompted to enter a string, which will be used to generate the keys.  
- The input string is converted into its **binary representation** using:

```python
result = ''.join(format(ord(i), '08b') for i in s)
```

> **Example Input:** `"hello"`  
> **Binary Representation:** `0110100001100101011011000110110001101111`

---

### **Step 2: Removing Every 8th Bit**
- DES removes parity bits during key generation. Similarly, this code eliminates every 8th bit from the binary string.

```python
for i in range(len(result)):
    if (i % 8 != 0):
        answer += result[i]
```

> **Result After Removal:** `110100001100101011011000110110001101111`

---

### **Step 3: Splitting the Binary String**
- The modified binary string is split into **two halves** to simulate DES's left and right halves.

```python
l = int(len(answer) / 2)
left = answer[:l]
right = answer[l:]
```

> **Left Half:** `11010000110010`  
> **Right Half:** `101101100011011`

---

### **Step 4: Bitwise Shifting and Key Generation**
- The code defines an array `lt` that holds shift values for each key.

```python
lt = [2, 3, 6, 7, 1, 6, 5, 9]
```

- In each loop iteration:
  - Both halves are shifted left by a specified number of bits.
  - The two halves are combined to form a new key.

```python
nl = int(left, 2)
nl = bin(nl << lt[i])
nr = int(right, 2)
nr = bin(nr << lt[i])
newKey = nr[num:] + nl[num:]
```

---

### **Step 5: Random Removal of Bits**
- To enhance randomness, the code randomly excludes 8 bits from each generated key.

```python
while (len(rm) != 8):
    r = random.randint(0, len(newKey) - 1)
    if r not in rm:
        rm.append(r)
```

- The remaining bits are collected as the final key.

```python
for i in range(len(newKey)):
    if i not in rm:
        newanswer += newKey[i]
```

---

### **Step 6: Key Output**
- Each generated key is stored in the `keys` list and displayed.

```python
for i in range(0, len(keys)):
    print("Key ", i + 1, " = ", keys[i])
```

---

## **Example Output**
```
Enter a string: hello
Key 1 =  10110000100110
Key 2 =  11010011100101
Key 3 =  10100110001101
Key 4 =  11010000111001
Key 5 =  00110101101001
Key 6 =  01001101000111
Key 7 =  11100010011010
Key 8 =  01101100101000
```

---

## **Key Components and Concepts**
- **Binary Conversion:** Converts characters into 8-bit binary values.  
- **Bitwise Shifting:** Uses `<<` (left shift) to manipulate binary data.  
- **Randomization:** Randomly excludes bits to introduce randomness.  
- **String Manipulation:** Efficiently processes binary strings to create keys.  

---

## **Potential Use Cases**
✅ Learning DES key generation logic.  
✅ Demonstrating bit manipulation and binary operations.  
✅ Generating randomized keys for testing and educational purposes.  

---

## **Limitations**
⚠️ This implementation is simplified and lacks the full DES key-scheduling logic.  
⚠️ The generated keys are **not actual DES keys** — they are inspired by DES logic.  
⚠️ For real encryption, full DES key generation rules must be implemented.  

---

## **Future Enhancements**
✅ Implement full DES key permutation and compression logic.  
✅ Introduce parity bit calculation for improved authenticity.  
✅ Add support for variable-length strings with padding techniques.  
✅ Integrate full DES encryption and decryption functionality.  

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
   python des.py
   ```

---
