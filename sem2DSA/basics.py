import random
def basic(n:{_it_, _sub_}):
    if n<0:
        return n
    print(n)
    return basic(n-1)

# print(basic(5))
basic(5)