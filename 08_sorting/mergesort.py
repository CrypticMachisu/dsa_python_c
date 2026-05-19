import random


def mergeSort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left_half = mergeSort(unsorted_list[:mid])
    right_half = mergeSort(unsorted_list[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while  i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def getValues():
    unsorted_list = random.sample(range(100),10)
    print(f"Unsorted {unsorted_list}")
    result = mergeSort(unsorted_list)
    print(f"Sorted {result}")

getValues()