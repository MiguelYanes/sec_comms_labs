"""
OK I'm so confident with this RSA stuff I'm using it to send messages to all my friends.

Can you figure out this message I've sent to all my friends?

Given: values.txt
"""
import binascii
from functools import reduce
from decimal import Decimal


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

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inv_mod(e, et):
    g, x = egcd(e, et)


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
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def mod_inverse(c, e, n, x):
    operation = find_invpow((c + x*n), e)
    try:
        print(str(int2string(operation)))
        solution = True
    except:
        print(str(x) + "\t" + str(operation))
        solution = False

    return solution


#crt = chinese_remainder([n1, n2, n3], [c1, c2, c3])
#message = find_invpow(crt, 3)
#m = int2string(message)
#print(m)


"""
c1 = m^e1 mod n1
c2 = m^e2 mod n2
c3 = m^e3 mod n3

c1 + x1*n1 = m^e1
root(e1, c1+x1*n1) = m

root(e1, c1+x1*n1) = root(e2, c2+x2*n2) = root(e3, c3+x3*n3) = m
"""

from functools import reduce

from Crypto.PublicKey import RSA

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii

from decimal import Decimal


def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)


def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


### X is the inverse of a mod b and Y is the inverse of b mod a
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


e1 = 3
n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c1 = 613757444204638278262310351562876531607487738717774407185252131147104492450160428757483976067628603514761619532764928239807564974590961450735755461481051283186240767490110455431475543041011912015289781128865893349142785039408178696523937605624371679605130950843591197358935516266254687080122972023592091964871

e2 = 3
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
c2 = 22657108022478695797486965023447848250682406595690518779077232421899889165762724488153241456845951937121308084431913683848889272505486222688188138471999687468256556616878979818168438370975399291696045396880071048188564812795530986969364538462949239012254381251606438993964309325106863727351705595563360310007

e3 = 3
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723
c3 = 311096000497881387953904724284440481805457233048982756757007020410000443330941053703716829538086459727079448020579354693958905904778381820371160626001594619419169121166486655254993091181369105737797409452734836563374374511516011594235202125201067840325349354834604004321427713901643355933701994777952169157646


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


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


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


crt = chinese_remainder([n1, n2, n3], [c1, c2, c3])
message = find_invpow(crt, 3)
m = int2string(message)
print(m)

