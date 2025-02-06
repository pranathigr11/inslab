def encrypt(text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'qwertyuiopasdfghjklzxcvbnm'
    text = text.lower()  # Convert to lowercase for uniformity

    encrypted_text = ""
    for char in text:
        if char in plain:
            encrypted_text += cipher[plain.index(char)]
        else:
            encrypted_text += char  # Preserve spaces and special characters
    return encrypted_text

def decrypt(text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'qwertyuiopasdfghjklzxcvbnm'

    decrypted_text = ""
    for char in text:
        if char in cipher:
            decrypted_text += plain[cipher.index(char)]
        else:
            decrypted_text += char  # Preserve spaces and special characters
    return decrypted_text

# Example usage
text = input("Enter the string of your choice: ")
enc = encrypt(text)
print("Encrypted text:", enc)

dec = decrypt(enc)
print("Decrypted text:", dec)
