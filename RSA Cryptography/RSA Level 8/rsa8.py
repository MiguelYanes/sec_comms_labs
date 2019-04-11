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

# m is the cubic root of ciphertext, calulated in wolframalpha
m = 52544240263489213319521825334419419391168959946460651046808951093331580864925337576823646249202867381357303129957

plaintext = int2string(m)
print("Decrypyed message: " + str(plaintext))
