def caesar_encrypt(plaintext, k):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char
    return result

plaintext = "NgoVanCuong"
k = 6
ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("k:", k)
print("Ciphertext:", ciphertext)
