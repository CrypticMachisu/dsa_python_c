import random

def bubbleSort(unsorted_list):
    number_of_elements: int = len(unsorted_list)
    for outer_loop in range(number_of_elements):
        for inner_loop in range(number_of_elements - 1 - outer_loop):
            if unsorted_list[inner_loop] > unsorted_list[inner_loop + 1]:
                temp = unsorted_list[inner_loop]
                unsorted_list[inner_loop] = unsorted_list[inner_loop + 1]
                unsorted_list[inner_loop + 1] = temp

    return unsorted_list

def getValues():
    # unsortedList = [5, 4, 3, 2, 1]
    unsortedList = random.sample(range(1,10),5)
    print(f"Unordered list is : {unsortedList}")
    sortedlist = bubbleSort(unsortedList)
    print(f"Sorted list {sortedlist}")

getValues()
