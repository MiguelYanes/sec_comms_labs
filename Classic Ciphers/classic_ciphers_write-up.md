Classic Ciphers
===============

In this lab we will implement in bash a series of methods to encrypt/decrypt messages 
using rotational ciphers.

For the ROT 5 we only need to rotate the digits 5 positions, getting the answer:

>Out digits are: 01234

<br/>

For ROT 13 we now need to rotate characters. As before, is as easy as defining the transformation
with 13 characters of difference:

>ROT 13 WAS USED BY MICROSOFT FOR ENCODING WINDOWS REGISTRYENTRIES

<br/>

The Caesar's cipher only rotates 3 characters, so to decode it we need to change to the 
preceding 3 characters:

>The original Caesar cipher alwaYs used a shift of three

<br/>

ROT 47 is a bit trickier, because it uses all ascii characters to rotate. If we take note of all
that characters to rotate, we get that the message is:

>With experience you will start to recognise the character sets of each encoding.

<br/>

To finish, we'll just define the aliases for all 4 rotational cipher implemented.