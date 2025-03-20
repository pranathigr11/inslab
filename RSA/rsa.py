def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, msg):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Finding e (public key exponent)
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break

    # Finding d (private key exponent)
    j = 0
    while True:
        if (j * e) % phi == 1:
            d = j
            break
        j += 1

    # Encryption
    c = (msg ** e) % n
    print("Encrypted message:", c)

    # Decryption
    decrypted_msg = (c ** d) % n
    print("Decrypted message:", decrypted_msg)

# Taking user inputs
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
msg = int(input("Enter a message (as an integer): "))

# Calling the function
RSA(p, q, msg)
