import random


def quickSort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    pivot = unsorted_list[0]

    left = []
    right = []

    for number in unsorted_list[1:]:
        if number <= pivot:
            left.append(number)
        else:
            right.append(number)

    return quickSort(left) + [pivot] + quickSort(right)

def getValues():
    unsorted_list = random.sample(range(100),10)
    print(f"Unsorted List {unsorted_list}")
    result = quickSort(unsorted_list)
    print(f"Sorted list {result}")

getValues()