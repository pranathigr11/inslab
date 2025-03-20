# **Diffie-Hellman Key Exchange Implementation**

This project demonstrates the **Diffie-Hellman Key Exchange Algorithm**, a fundamental cryptographic protocol used for securely exchanging cryptographic keys over a public channel. The code provided allows two users (Alice and Bob) to securely compute a shared secret key using modular arithmetic and discrete logarithms.

---

## **How It Works**
The Diffie-Hellman algorithm involves the following steps:

### **Step 1: Input Values**
The program prompts the user to provide the following inputs:

- **`q`** — A **prime number** (a crucial parameter for the modular arithmetic).  
- **`a`** — A **primitive root** of the prime number `q` (used to generate public keys).  
- **`Xa`** — The **private key** for User A (kept secret).  
- **`Xb`** — The **private key** for User B (kept secret).

> Example Input:  
```
Enter a prime number: 23
Enter a primitive root: 5
Enter the private key of A: 6
Enter the private key of B: 15
```

---

### **Step 2: Calculating Public Keys**
Using the given values, the program computes the **public keys** for both users using the formula:

\[
Y = a^{X} \mod q
\]

Where:
- `Y` = Public Key
- `a` = Primitive Root
- `X` = Private Key
- `q` = Prime Number

**Code Snippet:**
```python
Ya = math.pow(a, Xa) % q
Yb = math.pow(a, Xb) % q
print("Public key of A : ", Ya)
print("Public key of B : ", Yb)
```

> Example Output:  
```
Public key of A: 8.0
Public key of B: 19.0
```

---

### **Step 3: Calculating Shared Secret Keys**
Each user calculates the **shared secret key** using the other user's public key:

- For User A:  
\[
K_A = Y_b^{X_a} \mod q
\]

- For User B:  
\[
K_B = Y_a^{X_b} \mod q
\]

**Code Snippet:**
```python
Ka = math.pow(Yb, Xa) % q
Kb = math.pow(Ya, Xb) % q
print("Shared key for A : ", Ka)
print("Shared key for B : ", Kb)
```

> Example Output:  
```
Shared key for A: 2.0
Shared key for B: 2.0
```

✅ The keys `Ka` and `Kb` must be **identical**, proving that both parties have successfully established a secure shared key.

---

### **Step 4: Understanding the Security**
- The **private keys** (`Xa` and `Xb`) are never shared publicly.
- The security of this algorithm relies on the **difficulty of computing discrete logarithms** in modular arithmetic.

---

## **Example Walkthrough**
### **Input**
```
Enter a prime number: 23
Enter a primitive root: 5
Enter the private key of A: 6
Enter the private key of B: 15
```

### **Output**
```
Public key of A: 8.0
Public key of B: 19.0
Shared key for A: 2.0
Shared key for B: 2.0
```

✅ The shared keys match, meaning the key exchange is successful.

---

## **Key Concepts**
🔹 **Prime Numbers** — Essential for ensuring secure modular arithmetic.  
🔹 **Primitive Root** — A number that generates all the numbers in the prime field when raised to different powers.  
🔹 **Public Keys** — Exchanged openly without compromising security.  
🔹 **Private Keys** — Remain secret and are never shared.  
🔹 **Shared Key** — The final agreed-upon key that both parties use for secure communication.

---

## **Potential Use Cases**
🔒 Secure communication protocols (e.g., HTTPS, SSH, VPNs).  
🔒 Key exchange in messaging apps like WhatsApp or Signal.  
🔒 Secure cloud storage and file sharing.  

---

## **Improvements & Enhancements**
✅ Add error handling for invalid inputs (e.g., non-prime `q`).  
✅ Improve key validation to ensure `a` is a valid primitive root.  
✅ Introduce larger prime values for enhanced security.  
✅ Implement additional cryptographic functions for encryption after key exchange.  

---

## **Prerequisites**
Ensure you have **Python 3.x** installed to run the code.

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
   python diffie_hellman.py
   ```
## **runcode**
https://onlinegdb.com/_q7Q9bHWM

---
