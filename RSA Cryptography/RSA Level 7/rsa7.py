"""
We've just got the public key this time.. don't think there is any way we can crack this one?

Given: public.key

Hint: FactorDB is your friend
"""
import binascii


n = 0
e = 0
ciphertext = 0

with (open("public.key", "r")) as f:
    for line in f:
        line = line.split('=')
        letter = line[0]
        if letter == 'n ':
            n = int(line[1])
        elif letter == 'e ':
            e = int(line[1])
        elif letter == 'Ciphertext ':
            ciphertext = int(line[1])

print("n: " + str(n))
print("e: " + str(e))
print("ciphertext: " + str(ciphertext))

# from factordb.com
p = 3133337
q = 25478326064937419292200172136399497719081842914528228316455906211693118321971399936004729134841162974144246271486439695786036588117424611881955950996219646807378822278285638261582099108339438949573034101215141156156408742843820048066830863814362379885720395082318462850002901605689761876319151147352730090957556940842144299887394678743607766937828094478336401159449035878306853716216548374273462386508307367713112073004011383418967894930554067582453248981022011922883374442736848045920676341361871231787163441467533076890081721882179369168787287724769642665399992556052144845878600126283968890273067575342061776244939


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


print("n: " + str(n))
print("e: " + str(e))
print("ciphertext: " + str(ciphertext))
print("p: " + str(p))
print("q: " + str(q))
# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute modular inverse of e
gcd, a, b = egcd(e, phi)
d = a
print(d)

m = pow(ciphertext, d, n)
plaintext = int2string(m)
print("Decrypyed message: " + str(plaintext))
