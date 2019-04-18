"""
OK no more extra bits of information for you. Good luck trying to solve this one.
Just a public key and a ciphertext so should be impossible.

Given: values.txt

Hint: what happens if M^e < n?

c = m^e mod n
If m^e < n, then the modulo is no applied
Then c = m^e, so m is the e root of c, if our case, m is the cubic root of c
"""
import binascii


n = 0
e = 0
ciphertext= 0

with (open("values.txt", "r")) as f:
    for line in f:
        line = line.split('=')
        letter = line[0]
        if letter == 'n':
            n = int(line[1])
        elif letter == 'e':
            e = int(line[1])
        elif letter == 'ciphertext ':
            ciphertext = int(line[1])


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


print("n: " + str(n))
print("e: " + str(e))
print("ciphertext: " + str(ciphertext))


def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


m = find_invpow(ciphertext, e)
print(m)

plaintext = int2string(m)
print("Decrypyed message: " + str(plaintext))
