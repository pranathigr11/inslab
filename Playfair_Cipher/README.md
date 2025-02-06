
---

# **Playfair Cipher Encryption in Python**

## **Overview**
This Python script implements the **Playfair Cipher**, a digraph substitution cipher where pairs of letters are encrypted based on a 5x5 matrix constructed from a keyword. The Playfair cipher is considered one of the earliest forms of encryption that replaces each letter of the plaintext in pairs, using the matrix key for the substitution.

## **Features**
- ✅ Encrypts a given plaintext using the **Playfair Cipher** algorithm.
- ✅ Handles case insensitivity by converting all input to uppercase.
- ✅ Replaces the letter "J" with "I" (as the Playfair cipher does not handle "J").
- ✅ If the plaintext has an odd number of characters, it appends an "X" to the last letter to form even pairs.
- ✅ Preserves spaces (by removing them) and other special characters.

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
cd inslab
```

### **4. Run the Code**
To run the Playfair Cipher encryption script:
```bash
python playfair_cipher.py
```

## **How It Works**
- **Key Matrix Creation**: A key matrix is created from the given keyword. The letters in the keyword are placed in the matrix in order, removing duplicates, and then the rest of the alphabet (excluding "J") is filled in.
- **Pairing**: The plaintext is paired into digraphs (pairs of two letters). If there’s an odd number of characters, an "X" is appended to the end.
- **Encryption Process**:
  - If both letters of the pair are in the same row, they are replaced by the letters to their immediate right.
  - If both letters are in the same column, they are replaced by the letters immediately below.
  - If the letters form a rectangle, each letter in the pair is replaced by the letter in the same row but in the other column of the rectangle.
- Non-alphabetical characters are removed before encryption.

## **Example Execution**

### **Input:**
```bash
Enter the plaintext: HELLO
Enter the key: KEYWORD
```

### **Output:**
```bash
Encrypted: GYFFWZ
```

## **Code Explanation**

### **Functions**
1. `create_playfair_matrix(key)`:
   - Creates a 5x5 matrix using the given `key` and the alphabet.
   - Removes duplicates in the `key` and excludes the letter "J" (replacing it with "I").

2. `find_position(matrix, char)`:
   - Finds the position (row, column) of a given character in the Playfair matrix.

3. `playfair_encrypt(plaintext, key)`:
   - Encrypts the `plaintext` using the Playfair cipher by breaking the text into pairs and applying the encryption rules described above.

## **Customization**
- You can modify the `key` value to change the encryption.
- The plaintext will be automatically converted to uppercase, and the letter "J" will be replaced with "I".
- If you want to add decryption functionality, you can create a similar function following the reverse steps of the encryption.

## **Requirements**
- **Python 3.x**

## **Additional Information**
The Playfair cipher can be extended to include a decryption function, or you could modify the script to handle input validation or add additional functionality, such as allowing the user to input a key and plaintext dynamically.

---

