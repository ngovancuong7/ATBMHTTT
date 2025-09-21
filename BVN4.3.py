from math import gcd

p = 17
q = 23
e = 5
n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = mod_inverse(e, phi)
print("Public key: (e =", e, ", n =", n, ")")
print("Private key: (d =", d, ", n =", n, ")")

message = "NgoVanCuong"

cipher = [pow(ord(char), e, n) for char in message]
print("Original message:", message)
print("Encrypted:", cipher)

decrypted = "".join([chr(pow(c, d, n)) for c in cipher])
print("Decrypted message:", decrypted)
