import hashlib
import random

def hash_function(key):
    """
    Hashing function

    Low 32 bits of an MD5 hash
    """

    # You don't need to understand this line, but give it a shot anyway
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff


def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0

        tried = {}

        while True:
            random_key = random.random()

            index = hash_function(random_key) % buckets

            if index not in tried:
                tried[index] = True
                tries += 1
            else:
                break

        print(f'{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}% full)')

how_many_before_collision(131072, 10)

