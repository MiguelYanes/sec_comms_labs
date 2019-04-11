"""
OK I'm so confident with this RSA stuff I'm using it to send messages to all my friends.

Can you figure out this message I've sent to all my friends?

Given: values.txt
"""

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
        elif letter == 'n2':
            n2 = int(line[1])
        elif letter == 'c2':
            c2 = int(line[1])
        elif letter == 'e3 ':
            e3 = int(line[1])
        elif letter == 'n3 ':
            n3 = int(line[1])
        elif letter == 'c3 ':
            c3 = int(line[1])


"""
c1 = m^e1 mod n1
c2 = m^e2 mod n2
c3 = m^e3 mod n3

c1 + x1*n1 = m^e1
root(e1, c1+x1*n1) = m

root(e1, c1+x1*n1) = root(e2, c2+x2*n2) = root(e3, c3+x3*n3) = m
"""
