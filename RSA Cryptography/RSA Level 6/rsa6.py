"""
We seem to be missing the decryption key d? Can you help us somehow decode the ciphertext?

We get: key.py
"""

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

print(e)
print(p)
print(q)
print(ciphertext)

n = p*q

phi = (p-1) * (q-1)
