import binascii

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

with (open("rsa1.txt","r")) as f:
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

message = "RSA isn't really that hard"

print ("n:"+str(n))
print ("e:"+str(e))

m = string2int(message)

ciphertext = pow(m, e, n)
print("Cipher text: " + str(ciphertext))

