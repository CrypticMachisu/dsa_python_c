import random

def max_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num  < minimum:
            minimum = num
        # print(f"Current min {minimum}")
        # print("Python 3")
    return minimum


def getValues():
    list = random.sample(range(50, 100),10)
    print(list)
    result = max_min(list)
    print(f"value is {result}")

getValues()
