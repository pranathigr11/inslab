# **Bit Manipulation Key Generator**

This project implements a **Key Generator** that takes a string as input and produces 8 unique keys using bit manipulation techniques. Each key is derived by manipulating the binary representation of the input string. This project is intended for learning purposes and demonstrates concepts such as binary operations, shifting, and randomization.

---

## **How It Works**
The code performs the following steps to generate 8 unique keys:

### **Step 1: User Input**
- The program prompts the user to enter a string.
- The input string is converted into its **binary representation** using this line:

```python
result = ''.join(format(ord(i), '08b') for i in s)
```

> Example Input: `"hello"`  
> Binary Representation: `0110100001100101011011000110110001101111`

---

### **Step 2: Removing Every 8th Bit**
- The code removes every 8th bit from the binary string (simulating parity bit removal or similar encoding logic).  

```python
for i in range(len(result)):
    if (i % 8 != 0):
        answer += result[i]
```

> Example Result After Removal: `110100001100101011011000110110001101111`

---

### **Step 3: Splitting the Binary String**
- The resulting binary string is split into **two halves**:

```python
l = int(len(answer) / 2)
left = answer[:l]
right = answer[l:]
```

> Example Left Half: `11010000110010`  
> Example Right Half: `101101100011011`

---

### **Step 4: Bitwise Shifting and Key Generation**
- The code defines an array `lt` that contains shift values for each key.

```python
lt = [2, 3, 6, 7, 1, 6, 5, 9]
```

- In each loop iteration:
  - Both the left and right halves are converted back into integers and shifted left by the corresponding value in `lt`.
  - The shifted values are combined to form a new potential key.

```python
nl = int(left, 2)
nl = bin(nl << lt[i])
nr = int(right, 2)
nr = bin(nr << lt[i])
newKey = nr[num:] + nl[num:]
```

---

### **Step 5: Random Removal of Bits**
- Eight random indices are chosen to exclude bits from the generated binary string to introduce randomness.

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
- **Binary Conversion:** Converting characters to 8-bit binary form.
- **Bitwise Shifting:** Using `<<` (left shift) to manipulate binary data.
- **Randomization:** Randomly excluding bits to enhance randomness.
- **String Manipulation:** Efficiently handling binary strings for key creation.

---

## **Potential Use Cases**
While this code is a learning project, here are some potential applications:
✅ Creating simple keys for encryption-like algorithms.  
✅ Generating randomized data for testing.  
✅ Understanding bitwise operations and binary data manipulation.  

---

## **Improvements & Future Enhancements**
To enhance this project, you could:
- Add error handling for invalid inputs.
- Implement a stronger randomization method.
- Allow dynamic selection of shift values instead of fixed `lt` values.
- Introduce encryption concepts like XOR operations for added complexity.

---

## **Prerequisites**
Ensure you have Python installed (version 3.x recommended).

---

## **How to Run**
1. Clone this repository:
   ```
   git clone <repository_link>
   ```
2. Navigate to the project directory:
   ```
   cd <project_directory>
   ```
3. Run the Python file:
   ```
   python key_generator.py
   ```

---

