import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
    return ciphertext

# Example usage
plaintext = "HELLO"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix
print("Encrypted:", hill_cipher_encrypt(plaintext, key_matrix))
