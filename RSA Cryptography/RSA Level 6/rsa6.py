"""
We seem to be missing the decryption key d? Can you help us somehow decode the ciphertext?

We get: key.txt
"""
import binascii


e = 0
p = 0
q = 0
ciphertext = 0

with (open("key.txt", "r")) as f:
    for line in f:
        line = line.split('=')
        letter = line[0]
        if letter == 'e ':
            e = int(line[1])
        elif letter == 'p ':
            p = int(line[1])
        elif letter == 'q ':
            q = int(line[1])
        elif letter == 'ciphertext ':
            ciphertext = int(line[1])


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


print(e)
print(p)
print(q)
print(ciphertext)

# compute n
n = p * q

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute modular inverse of e
gcd, a, b = egcd(e, phi)
d = a
print(d)

m = pow(ciphertext, d, n)
plaintext = int2string(m)
print("Decrypyed message: " + str(plaintext))
