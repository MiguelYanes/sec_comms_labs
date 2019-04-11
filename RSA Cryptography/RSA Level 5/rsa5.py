"""
Can you decode this one?

Attached file: key.txt
"""

import operator
import binascii


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


p = 0
q = 0
dp = 0
dq = 0
pinv = 0
qinv = 0
ciphertext = 0

with (open("key.txt", "r")) as f:
    for line in f:
        line = line.split('=')
        letter = line[0]
        if letter == 'p ':
            p = int(line[1])
        elif letter == 'q ':
            q = int(line[1])
        elif letter == 'dp ':
            dp = int(line[1])
        elif letter == 'dq ':
            dq = int(line[1])
        elif letter == 'pinv ':
            pinv = int(line[1])
        elif letter == 'qinv ':
            qinv = int(line[1])
        elif letter == 'ciphertext ':
            ciphertext = int(line[1])


m1 = pow(ciphertext, dp, p)
print("m1: " + str(m1))
m2 = pow(ciphertext, dq, q)
print("m2: " + str(m2))
h = operator.mod((qinv * (m1 - m2)), p)
print("h: " + str(h))
m = m2 + h*q
print("m: " + str(m))
print("message: " + int2string(m))
