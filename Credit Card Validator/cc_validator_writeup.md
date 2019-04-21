Credit Card Validator
=====================

Lab 9 - Credit Card Verifier

Miguel Yanes Fernández - B00122692

<br/>
Scenario:
<br/><br/>
Create a program to manage credit card numbers. The program should have the following modes:

1. Verify: Take a credit card number as input and output if it is a valid or invalid credit card number.

2. Vendor: Again take a credit card number as input and output the issuing vendor

3. Checksum:  Given just the first portion of a credit card calculate the checksum

4. Generate: Select the issuing vendor, then generate a random valid credit card 


<br/><br/>
Solution:
<br/><br/>
As this required source code for this lab is a bit longer than in the others, I decided to create a class named CreditCardValidator, 
so i can define all the required methods inside the same class. 
I also created a custom csv file to store all the information about the vendors. The format of the file is the following:

* First, the name of the vendor

* Length (or lengths) of the credit card numbers provided from that vendor. Ranges separated with `-` and sequences separated with `.`

* Finally, all the possible ranges of that vendor. Ranges separated with `-` and sequences with commas (`,`).

[Source](https://en.wikipedia.org/wiki/Payment_card_number)

Alongside with this file, I also created a method (`read_vendors_file()`) to read, filter, and store the information of the file in 
a class variable named `vendors_list`

<br/><br/>
1. Verify

The credit card verifying process uses the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) to determine whether the number 
is valid or not. This algorithm checks the sum of all digits multiplied by a variable depending of their position in the number 
(if the digit is in an even position, will be multiplied by 2, if it's in an odd position, multiplied by 1). If the result is a
two digit number, both digits of that number will be added up. The result sum of all operations in all digits is the number we need.
Then, the last digit of the credit card, called the checksum, should be one that added with the previous calculated sum, will be 
a multiple of 10. If it ends in 0, then the credit card number is correct. If not, the number is invalid.

To implement the credit number verify, I created two different methods. One of them (`calculate_checksum(credit_number)`) is to calculate the sum of all digits (except
for the last one in this case), and another method (`verify(credit_number)`) to check if the sum with the checksum if a multiple of 10.

<br/>

2. Vendor

The `vendor(credit_number)` method will use the class variable `vendors_list`. It iterates the vendors vector and checks, 
for each vendor, all possible provided ranges. The algorithm will check an increasing ammount of digits of both the 
credit card number, an the vendor range. If the selected digits of the credit card number, are the same length as the range 
provided, it will check if its similar (or in cases of ranges of ranges (separated with `-`), it will check all range).
Also, the method stores the longest match found, and for every match with a higher number of characters, it will store the 
new one. Once it finishes scanning all vendors, it returns the vendor with the highest length match.

<br/>

3. Checksum

This option will return the required checksum to make the selected credit number valid. It uses the already defined method 
`calculate_checksum(credit_number)`, and it checks if the returned value is divisible by 10. If it's not, it substracts 10
to the returned value; if not, it just returns the value.

<br/>

4. Generate

The last main option is to generate a valid credit card number of a selected vendor. After listing all available vendors,
the user has to choose one. Once a vendor is chosen, the method `generate(vendor)` will select a random number length from 
the ones provided by the selected vendor, and a random initial range also selected from the ones offered by the vendor. 
Then, it generates the required amount of random digits, except for the last one. With the method `checksum(credit_number)`
it gets the required checksum to make the number digit. Once the number is complete, it is returned to the user.