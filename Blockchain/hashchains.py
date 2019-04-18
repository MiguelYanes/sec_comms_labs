#!/usr/bin/env python3
import hashlib


def hash(string):
    """
    Calculate MD5 hash of the given input string
    :param string: string to hash
    :return: hashed string (MD5)
    """
    hash = hashlib.md5()
    hash.update(str.encode(string))

    result = hash.hexdigest()
    print(result)

    return result


def calculate_seed(input):
    """
    Create the seed to hash of the given input. The method will replace all lower case letters with
    upper case letters, and vice versa.
    :param input: input string
    :return: calculated seed
    """
    seed = ""
    for char in input:
        if char.islower():
            seed += char.upper()
        elif char.isupper():
            seed += char.lower()
        else:
            seed += char

    print("Seed: " + seed)
    return seed


def get_hashes(seed, iterations):
    """
    Get all MD5 hashes (and hashes of hashes) with the given seed and the specified number of iterations
    :param seed: initial seed to hash
    :param iterations: number of times to re-hash
    :return: penultimate hash (the last hash is the challenge)
    """
    prev_seed = ""
    seed = seed
    for i in range(0, iterations + 1):
        prev_seed = seed
        seed = hash(seed)

    return prev_seed


def get_result(username):
    """
    Method to automate the process. First, generates the seed, then gets the target hash and prints it
    It iterates 1100 times because it was calculated to be the correct number of iterations (detailed
    explanation in the write-up).
    :param username: username to calculate the target hash
    :return: target hash
    """
    seed = calculate_seed(username)
    prev_seed = get_hashes(seed, 1100)
    print("\nTarget seed: ")
    print(prev_seed)
    return prev_seed


user = input("Enter username: ")
get_result(user)
