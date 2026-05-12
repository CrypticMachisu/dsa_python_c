import random

def linear_search(values, target):
    for item in range(len(values)):
        if values[item] == target:
            return item
    return -1

def get_values():
    values = random.sample(range(-10, 10),5)
    print(f"The list is {values}")
    target = int(input("Enter value to search "))
    result = linear_search(values, target)
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Not found")

get_values()


