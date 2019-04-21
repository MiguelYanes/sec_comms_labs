"""
OK I'm so confident with this RSA stuff I'm using it to send messages to all my friends.

Can you figure out this message I've sent to all my friends?

Given: values.txt
"""
import binascii
from functools import reduce


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


e1 = 0
n1 = 0
c1 = 0

e2 = 0
n2 = 0
c2 = 0

e3 = 0
n3 = 0
c3 = 0

with (open("values.txt", "r")) as f:
    for line in f:
        line = line.split('=')
        letter = line[0]
        if letter == 'e1 ':
            e1 = int(line[1])
        elif letter == 'n1 ':
            n1 = int(line[1])
        elif letter == 'c1 ':
            c1 = int(line[1])
        elif letter == 'e2 ':
            e2 = int(line[1])
        elif letter == 'n2 ':
            n2 = int(line[1])
        elif letter == 'c2 ':
            c2 = int(line[1])
        elif letter == 'e3 ':
            e3 = int(line[1])
        elif letter == 'n3 ':
            n3 = int(line[1])
        elif letter == 'c3 ':
            c3 = int(line[1])


def find_invpow(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


crt = chinese_remainder([n1, n2, n3], [c1, c2, c3])
message = find_invpow(crt, 3)
m = int2string(message)
print("Message: " + m)

