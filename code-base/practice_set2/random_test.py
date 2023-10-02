import random

def infinite_random_numbers():
    while True:
        yield random.randint(1, 100)

# Usage:
gen = infinite_random_numbers()
for _ in gen:
    print(next(gen))