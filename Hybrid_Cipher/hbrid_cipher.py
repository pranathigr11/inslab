import math

# Vigenère Cipher (Substitution)
def vigenere_cipher(text, key, encrypt=True):
    """Encrypts or decrypts text using the Vigenère cipher with the given key."""
    result = []
    key = key.upper()
    key_length = len(key)
    shift = 1 if encrypt else -1

    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_shift = ord(key[i % key_length]) - ord('A')
            new_char = chr((ord(char) - base + shift * key_shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(result)

# Columnar Transposition Cipher
def columnar_transposition_encrypt(text, key):
    """Encrypts using Columnar Transposition with given key."""
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Order of key letters
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill grid row-wise
    index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    # Read columns in key order
    encrypted_text = ''.join(grid[row][col] for col in key_order for row in range(num_rows) if grid[row][col] != ' ')
    return encrypted_text

def columnar_transposition_decrypt(text, key):
    """Decrypts Columnar Transposition cipher with given key."""
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
   
    # Create an empty grid
    grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
   
    # Fill columns based on key order
    index = 0
    for col in key_order:
        for row in range(num_rows):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    # Read row-wise
    decrypted_text = ''.join(grid[row][col] for row in range(num_rows) for col in range(num_cols) if grid[row][col] != ' ')
    return decrypted_text

# Hybrid Cipher Functions
def hybrid_encrypt(text, vigenere_key, transposition_key):
    """Applies Vigenère cipher followed by Columnar Transposition."""
    vigenere_encrypted = vigenere_cipher(text, vigenere_key, encrypt=True)
    columnar_encrypted = columnar_transposition_encrypt(vigenere_encrypted, transposition_key)
    return columnar_encrypted

def hybrid_decrypt(text, vigenere_key, transposition_key):
    """Reverses Columnar Transposition, then reverses Vigenère cipher."""
    columnar_decrypted = columnar_transposition_decrypt(text, transposition_key)
    vigenere_decrypted = vigenere_cipher(columnar_decrypted, vigenere_key, encrypt=False)
    return vigenere_decrypted

# Example Usage
plaintext = "SECUREHYBRID"
vigenere_key = "KEY"  # Key for Vigenère Cipher
transposition_key = "4312"  # Key for Columnar Transposition Cipher

encrypted_text = hybrid_encrypt(plaintext, vigenere_key, transposition_key)
decrypted_text = hybrid_decrypt(encrypted_text, vigenere_key, transposition_key)

print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
