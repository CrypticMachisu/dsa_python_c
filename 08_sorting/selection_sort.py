import random

def selectionSort(unsorted_list):
    number_of_elements = len(unsorted_list)
    for outer_loop in range(number_of_elements):
        minimum_index = outer_loop
        for inner_loop in range(outer_loop + 1,number_of_elements):
            if unsorted_list[inner_loop] < unsorted_list[minimum_index]:
                minimum_index = inner_loop

        temp = unsorted_list[outer_loop]
        unsorted_list[outer_loop] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = temp
        # print(f"After {unsorted_list}")

    return unsorted_list

def getValues():
    unsorted_list = random.sample(range(1,100),5)
    # unsorted_list = [5, 4, 3, 2, 1]
    print(f"Unordered list is : {unsorted_list}")
    sortedlist = selectionSort(unsorted_list)
    print(f"Sorted list {sortedlist}")

getValues()