def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha(): 
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + k) % 26 + base
            ciphertext += chr(shifted)
        else:
            ciphertext += ch
    return ciphertext

P = "NgoVanCuong"
k = 6
C = caesar_encrypt(P, k)
print("Plaintext :", P)
print("Ciphertext:", C)
