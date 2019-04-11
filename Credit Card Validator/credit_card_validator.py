# verify: take number as input, output if it's valid or not
# vendor: take number as input, output issuing vendor
# checksum: given first portion of a credit card, calculate the checksum
# generate: select issuing vendor, then generate a random valid credit card
import time
import random


class CreditCardValidator:
    def __init__(self):
        self.vendors_list = []

    def calculate_checksum(self, credit_number):
        digits = str(credit_number)
        products = []
        checksum = 0
        digits = digits[::-1]
        i = 1
        for digit in digits:
            if i % 2 == 0:
                result = int(digits[i - 1]) * 2
                if len(str(result)) == 2:
                    res = 0
                    for num in str(result):
                        res += int(num)
                    result = res
            else:
                result = digits[i - 1]
            products.append(result)
            i += 1

        for product in products:
            checksum += int(product)
        return checksum

    def verify(self, credit_number):
        checksum = self.calculate_checksum(credit_number)
        if checksum % 10 == 0:
            return True
        return False

    def read_vendors_file(self):
        self.vendors_list = []

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

                    self.vendors_list.append(list)

    def vendor(self, credit_number):
        target_vendor = ""
        max_digits = 0
        for vendor in self.vendors_list:
            vendor_range = []
            for num_range in vendor[2]:
                if '-' in num_range:
                    limits = num_range.split('-')
                    if int(str(credit_number)[:len(limits[0])]) > int(limits[0]) and \
                       int(str(credit_number)[:len(limits[0])]) < int(limits[1]):
                            for num in range(int(limits[0]), int(limits[1])):
                                vendor_range.append(num)
                else:
                    vendor_range.append(num_range)

            digit_count = 1
            for digit in str(credit_number):
                if digit_count <= 8:
                    for num_range in vendor_range:
                        if len(str(num_range)) is digit_count:
                            if str(credit_number)[:digit_count] == str(num_range):
                                if digit_count > max_digits:
                                    target_vendor = vendor[0]
                                    max_digits = digit_count
                    digit_count += 1
                else:
                    break

        if target_vendor != "":
            return target_vendor
        return None

    def checksum(self, credit_number):
        sum_before = self.calculate_checksum(credit_number)
        remainder = sum_before % 10

        correct_sum = False
        while not correct_sum:
            chechsum = 0

            num1 = random.randint(0, 9)
            num1_prod = num1 * 2
            if len(str(num1_prod)) == 2:
                res = 0
                for num in str(num1_prod):
                    res += int(num)
                num1_prod = res

            num2_prod = random.randint(0, 9)

            num3 = random.randint(0, 9)
            num3_prod = num3 * 2
            if len(str(num3_prod)) == 2:
                res = 0
                for num in str(num3_prod):
                    res += int(num)
                num3_prod = res
            num4_prod = random.randint(0, 9)

            checksum = num1_prod + num2_prod + num3_prod + num4_prod
            if (checksum % 10 + remainder) % 10 == 0:
                correct_sum = True
        return num1, num2_prod, num3, num4_prod

    def get_list_vendors(self):
        vendors = []
        for vendor in self.vendors_list:
            vendors.append(vendor[0])
        return vendors

    def generate(self, vendor):
        credit_number = 0
        for vendors in self.vendors_list:
            if vendors[0] == vendor:
                # Get length
                length = vendors[1]
                lengths = []
                if '.' in length:
                    length = length.split('.')
                    for l in length:
                        lengths.append(l)
                elif '-' in length:
                    length = length.split('-')
                    for l in range(length[0], length[1]):
                        lengths.append(l)
                else:
                    lengths.append(length)

                rndm_choice = random.randint(0, len(lengths)-1)
                selected_length = int(lengths[rndm_choice]) - 4  # -4 because of the checksum

                # Get vendor range
                vendor_range = []
                for num_range in vendors[2]:
                    if '-' in num_range:
                        limits = num_range.split('-')
                        for num in range(int(limits[0]), int(limits[1])):
                            vendor_range.append(num)
                    else:
                        vendor_range.append(num_range)

                rndm_choice = random.randint(0, len(vendor_range)-1)
                selected_range = vendor_range[rndm_choice]

                # Generate numbers
                credit_number = selected_range
                for digit in range(0, int(selected_length) - int(len(str(selected_range)))):
                    number = random.randint(0, 9)
                    credit_number += str(number)

                # Get checksum
                num1, num2, num3, num4 = self.checksum(credit_number)
                credit_number += str(num1)
                credit_number += str(num2)
                credit_number += str(num3)
                credit_number += str(num4)

        return credit_number


ccvalidator = CreditCardValidator()
exit = False

while not exit:
    print("---------------------------------------------------")
    print("\n\tCredit Card Validation software")
    print("\nAvailable options:")
    print("\t1: Verify credit card number")
    print("\t2: Check vendor")
    print("\t3: Checksum of incomplete credit card number")
    print("\t4: Generate credit card number")
    print("\t5: Exit")
    print("---------------------------------------------------")
    choice = input("\nSelect an option: ")
    if choice == '1':
        credit_number = input("\nType the credit card number to verify:\n\t> ")
        if ccvalidator.verify(credit_number):
            print("\nThe number is valid\n")
        else:
            print("\nThe number is invalid\n")
        time.sleep(1)
        print("\n\n")
    elif choice == '2':
        if not ccvalidator.vendors_list:
            ccvalidator.read_vendors_file()
            print("\nReading vendors file...\n")
        credit_number = input("\nType the credit card number to check:\n\t> ")
        vendor = ccvalidator.vendor(int(credit_number))
        if vendor:
            print("\nThe vendor is: " + vendor)
        else:
            print("\nUnknown vendor")
        time.sleep(1)
        print("\n\n")
    elif choice == '3':
        credit_number = input("\nType the credit card to check the checksum:\n\t> ")
        num1, num2, num3, num4 = ccvalidator.checksum(credit_number)
        print("\nCalculated random checksum: " + str(num1) + str(num2) + str(num3) + str(num4))
    elif choice == '4':
        if not ccvalidator.vendors_list:
            ccvalidator.read_vendors_file()
            print("\nReading vendors file...\n")
        vendors = ccvalidator.get_list_vendors()
        print("\n")
        for vendor in vendors:
            print("\t" + vendor)

        selected_vendor = input("Select vendor for the generated credit card:\n\t> ")
        if selected_vendor in vendors:
            generated_number = ccvalidator.generate(selected_vendor)
            print("\nGenerated credit card number:\n\t" + str(generated_number))
        else:
            print("\nInvallid vendor")
        time.sleep(1)
        print("\n\n")
    elif choice == '5':
        exit = True
    else:
        print("\nInvalid option\n")

print("\nExiting the program\n")

visa = 4549652917551085
mastercard = 5222282338448546
discover = 6011170232417993
americanexpress = 376718830351907
jcb = 3588195270040563
invented = 84567891234569

print(ccvalidator.verify(visa))
print(ccvalidator.verify(mastercard))
print(ccvalidator.verify(discover))
print(ccvalidator.verify(americanexpress))
print(ccvalidator.verify(jcb))
print(ccvalidator.verify(invented))

ccvalidator.read_vendors_file()
print("---------------")
print(ccvalidator.vendor(visa))
print(ccvalidator.vendor(mastercard))
print(ccvalidator.vendor(discover))
print(ccvalidator.vendor(americanexpress))
print(ccvalidator.vendor(jcb))
print(ccvalidator.vendor(invented))

print(ccvalidator.checksum(visa))
print(ccvalidator.checksum(invented))
