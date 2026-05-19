import random

def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2

        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def get_values():
    values = random.sample(range(1, 10),5)
    values = sorted(values)
    print(f"The list is {values}")
    target = int(input("Enter value to search "))
    result = binary_search(values, target)
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Not found")

get_values()
