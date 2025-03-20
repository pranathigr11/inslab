# **RSA Encryption and Decryption in Python**

This project implements the **RSA Algorithm**, a widely used asymmetric cryptographic technique for secure data transmission. The RSA algorithm uses a pair of keys — **public key** for encryption and **private key** for decryption.

---

## **How It Works**
The RSA algorithm follows these steps:

1. **Input Prime Numbers (`p` and `q`)**  
2. **Calculate `n` and `phi(n)`**  
3. **Find Public Key (`e`)**  
4. **Find Private Key (`d`)**  
5. **Encrypt the Message**  
6. **Decrypt the Encrypted Message**  

---

## **Step 1: Input Values**
The program prompts for:

- **`p`** — A prime number.  
- **`q`** — Another prime number.  
- **`msg`** — The message (entered as an integer for simplicity).  

> Example Input:  
```
Enter the value of p: 17
Enter the value of q: 11
Enter a message (as an integer): 88
```

---

## **Step 2: Calculate `n` and `phi(n)`**
The product of `p` and `q` determines `n`, which is part of the public key:

```python
n = p * q
phi = (p - 1) * (q - 1)
```

For the example above:  
```
n = 17 * 11 = 187
phi = (17 - 1) * (11 - 1) = 160
```

---

## **Step 3: Find Public Key (`e`)**
The public exponent `e` is chosen such that:

- `1 < e < phi(n)`  
- `gcd(e, phi(n)) = 1` (i.e., `e` and `phi` are coprime)  

```python
for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break
```

For this example:  
```
e = 3
```

---

## **Step 4: Find Private Key (`d`)**
The private key `d` satisfies the equation:

\[
(d \times e) \mod \phi(n) = 1
\]

```python
j = 0
while True:
    if (j * e) % phi == 1:
        d = j
        break
    j += 1
```

For this example:  
```
d = 107
```

---

## **Step 5: Encryption Process**
The ciphertext `c` is calculated using the formula:

\[
c = (msg^e) \mod n
\]

```python
c = (msg ** e) % n
print("Encrypted message:", c)
```

For example:
```
Encrypted message: 11
```

---

## **Step 6: Decryption Process**
The decrypted message is calculated using:

\[
decrypted\_msg = (c^d) \mod n
\]

```python
decrypted_msg = (c ** d) % n
print("Decrypted message:", decrypted_msg)
```

For example:
```
Decrypted message: 88
```

---

## **Step 7: Example Output**
### **Input**
```
Enter the value of p: 17
Enter the value of q: 11
Enter a message (as an integer): 88
```

### **Output**
```
Encrypted message: 11
Decrypted message: 88
```

✅ The decrypted message matches the original message, confirming successful encryption and decryption.

---

## **Key Concepts of RSA Algorithm**
🔹 **Prime Numbers (`p` and `q`)** — Essential for generating secure keys.  
🔹 **Modular Arithmetic** — Provides encryption and decryption security.  
🔹 **Public and Private Keys** — Ensures asymmetric encryption where only the intended recipient can decrypt the message.  

---

## **Potential Use Cases**
✅ Secure email communication.  
✅ Digital signatures for authenticity and integrity.  
✅ Encrypting sensitive data during online transactions.  

---

## **Limitations**
⚠️ RSA encryption for large messages may require additional padding techniques.  
⚠️ The algorithm is slower than symmetric encryption methods for bulk data.  
⚠️ Weak prime numbers can compromise security — ensure strong prime selection.  

---

## **Improvements & Enhancements**
✅ Implement message-to-integer conversion for improved text support.  
✅ Introduce key size selection for enhanced security.  
✅ Add error handling for non-prime values or invalid user inputs.  
✅ Improve performance by optimizing modular exponentiation.  

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
   python rsa.py
   ```
## **runcode**
https://onlinegdb.com/ZKAAU9clp

---
