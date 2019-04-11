import hashlib


def hash(string):

    hash = hashlib.md5()
    hash.update(string)

    result = hash.hexdigest()
    print(result)

    return result


def calculate_seed(input):
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
    prev_seed = ""
    seed = seed
    for i in range(0, iterations + 1):
        prev_seed = seed
        seed = hash(seed)

        if seed == "c89aa2ffb9edcc6604005196b5f0e0e4":
            return prev_seed


def get_result(username):
    seed = calculate_seed(username)
    prev_seed = get_hashes(seed, 1100)
    print("\nTarget seed: ")
    print(prev_seed)
    return prev_seed


get_result("ECSC")
