# verify: take number as input, output if it's valid or not
# vendor: take number as input, output issuing vendor
# checksum: given first portion of a credit card, calculate the checksum
# generate: select issuing vendor, then generate a random valid credit card
vendors_list = []


def verify(credit_number):
    digits = str(credit_number)
    products = []
    checksum = 0
    digits = digits[::-1]
    i = 1
    for digit in digits:
        if i % 2 == 0:
            result = int(digits[i-1]) * 2
            if len(str(result)) == 2:
                res = 0
                for num in str(result):
                    res += int(num)
                result = res
        else:
            result = digits[i-1]
        products.append(result)
        i += 1

    for product in products:
        checksum += int(product)

    if checksum % 10 == 0:
        return True
    return False


def read_vendors_file():
    vendors_list = []

    with open("vendors.txt", "r") as file:
        for line in file:
            values = line.split(',')
            if values[0] == '#':
                pass
            else:
                vendor_name = values[0]
                length = values[1]
                ranges = []
                for i in range(2, len(values)):
                    if values[i][-1:] == '\n':
                        values[i] = values[i][:-1]
                    ranges.append(values[i])
                list = []
                list.append(vendor_name)
                list.append(length)
                list.append(ranges)

                vendors_list.append(list)
    print(vendors_list)


def vendor(credit_number):
    pass


def checksum():
    pass


def generate():
    pass


visa = 4549652917551085
mastercard = 5222282338448546
discover = 6011170232417993
americanexpress = 376718830351907
jcb = 3588195270040563

print(verify(visa))
print(verify(mastercard))
print(verify(discover))
print(verify(americanexpress))
print(verify(jcb))

read_vendors_file()
