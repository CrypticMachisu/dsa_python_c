import random

def basic(n):
    if n < 1:
        return n

    print(n)
    return basic(n - 1) # last line

basic(5)
















# num = random.randint(1, 10)
# print(f"The number is {num}")
# basic(num)