def caesar_cipher_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decryption(encryption, shift):
    result = ""
    for char in encryption:  
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)  
        else:
            result += char
    return result

# Example usage
text = input("enter the text : ")
shift = int(input("enter the shift : "))
encryption = caesar_cipher_encryption(text, shift)
print("Encrypted:", encryption)

decryption = caesar_cipher_decryption(encryption, shift)
print("Decrypted:", decryption)
