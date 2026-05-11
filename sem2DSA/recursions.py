import typing
import random
# Direct Recursion
def basic(n):
    if n<0:
        return n
    print(n)
    return basic(n-1)

basic(5)

# Indirect Recursion
def a(n):
    if n > 0:
        print(f"Inside a {n}")
        return b(n-1)
    
    # if n < 1:
    #     return n
    # else:
    #     print(f"Inside a {n}")
    #     return b(n-1)
    
def b(n):
    if n > 0:
        print(f"Inside b {n}")
        return a(n-1)
    
a(5)
# Tail Recursion
def tail_recursion(n):
    if n < 1:
        return n
    
    print(n)
    return tail_recursion(n-1)

tail_recursion(5)

# Head Recursion
def head_recursion(n):
    if n < 1:
        return n
    
    head_recursion(n-1)
    print(n)
    
head_recursion(5)

# Linear Search
def linear_search(values, target):
    for item in range(len(values)):
        if values[item] == target:
            return item
    
    return -1

def get_values():
    values = random.sample(range(50, 100), 10)
    print(f"The list of values is {values}")
    target = int(input("Enter the target value: "))
    result = linear_search(values, target)
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print("The value is not found in the list")

get_values()

# Binary Search
def binary_search(values, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print(f"low: {low}, high: {high}, mid: {mid}")
    if values[mid] == target:
        # Base Case
        return mid
    elif values[mid] < target:
        return binary_search(values, target, mid+1, high)
    else:
        return binary_search(values, target, low, mid-1)

def get_values():
    values = random.sample(range(50, 100), 10)
    values = sorted(values)
    print(f"The list of values is {values}")
    target = int(input("Enter the target value: "))
    result = binary_search(values, target, low = 0, high = len(values))
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print("The value is not found in the list")

get_values()