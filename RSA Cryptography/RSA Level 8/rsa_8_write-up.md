RSA Level 8
===========

In level 8 we get again only the values of n, e and ciphertext. 

In this case, we can't factorize n, so we need to find another option. The solution consists in 
a weakness caused because the value of m^e is lower than n (so the modulo doesn't apply to 
the original ciphertext). This is caused because the original message is too small, 
even smaller than n.

What we have now is that the ciphertext key is equal to m^e, which in this case is 3.
This is another weakness because we just need to calculate the cubic root of c to get 
the original message.

>Decrypyed message: We always need to watch the size of our message
