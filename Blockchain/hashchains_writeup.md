Hash Chains
===========

Lab 8 - Simple Blockchain


Scenario:

*You've registered for an online service that uses hash chains.
You've registered as user 'n00B' and have been given the hash chain seed 654e1c2ac6312d8c6441282f155c8ce9
Use the given information to figure out how to authenticate as the user 'ESCS' for the given challenge hash c89aa2ffb9edcc6604005196b5f0e0e4
i.e. Find the hash that hashes to this - This hash will be your solution*

Solution:

We'll use the python library hashlib to calculate the MD5 hash.
First, we need to know the seed of the hashing algorithm. We can get the seed with a web search of the given MD5 hash for the 
seed generated for the user 'nOOB'. With the [reverse check of the MD5](https://md5.gromweb.com/?md5=654e1c2ac6312d8c6441282f155c8ce9)
we get that the seed is 'Noob'. The seed generation consists then in replacing lower case letters with upper case letters, 
and vice versa.

With that known, we can implement out own algorithm to generate the seed of a given username:

tbd . . .
