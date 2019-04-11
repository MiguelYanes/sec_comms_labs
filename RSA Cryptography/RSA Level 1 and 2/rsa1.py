"""
Use the RSA values in the attached file to encrypt the given message and submit your first flag.

Message = RSA isn't really that hard

Submit your flag in the following format: ZD{encrypted_message}

your encrypted message should be a big number in decimal format.

Attached file: rsa1.txt
"""

import binascii


def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)


with (open("rsa1.txt", "r")) as f:
    for line in f:
        letter = line[0]
        if letter == 'n':
            n = int(line[3:])
        elif letter == 'e':
            e = int(line[3:])
        elif letter == 'd':
            d = int(line[3:])
        elif letter == 'p':
            p = int(line[3:])
        elif letter == 'q':
            q = int(line[3:])

message = b"RSA isn't really that hard"

print("n:"+str(n))
print("e:"+str(e))

m = string2int(message)

ciphertext = pow(m, e, n)
print("Cipher text: " + str(ciphertext))
