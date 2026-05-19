import random


def insertion_sort(unsorted_list):
    number_of_elements = len(unsorted_list)

    # Start from the second element (index 1) and move through the list
    for current_index in range(1, number_of_elements):
        current_value = unsorted_list[current_index]

        # Move the current value to its correct position in the sorted part
        while unsorted_list[current_index - 1] > current_value and current_index > 0:
            # Swap the current value with the one before it

            temp = unsorted_list[current_index]
            unsorted_list[current_index] = unsorted_list[current_index - 1]
            unsorted_list[current_index - 1] = temp

            # numbers[current_index], numbers[current_index - 1] = numbers[current_index - 1], numbers[current_index]

            # move backwards to the beginning
            current_index -= 1
            # current_index = current_index - 1

    return unsorted_list


# 10 unique numbers from 1 to 99
random_list = random.sample(range(1, 100), 10)

print("Unsorted list:", random_list)
sorted_list = insertion_sort(random_list.copy())
print("Sorted list:", sorted_list)