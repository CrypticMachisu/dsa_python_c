# basic list operations in Python

def create_list():
    """Create a simple list"""
    numbers = [1, 2, 3, 4, 5]
    print("Created list:", numbers)


def access_elements():
    """Access elements using index"""
    fruits = ["apple", "banana", "cherry"]
    print("First element:", fruits[0])
    print("Last element:", fruits[-1])


def modify_elements():
    """Modify elements in a list"""
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    fruits[1] = "orange"
    print("Modified list:", fruits)


def add_elements():
    """Add elements to a list"""
    numbers = [1, 2, 3]

    numbers.append(4)  # add to end
    print("After append:", numbers)

    numbers.insert(1, 10)  # insert at index
    print("After insert:", numbers)


def remove_elements():
    """Remove elements from a list"""
    numbers = [1, 2, 3, 4, 5]

    numbers.remove(3)  # remove specific value
    print("After remove:", numbers)

    popped = numbers.pop()  # remove last element
    print("Popped element:", popped)
    print("After pop:", numbers)


def list_slicing():
    """Demonstrate slicing"""
    numbers = [1, 2, 3, 4, 5]

    print("First 3 elements:", numbers[:3])
    print("Last 2 elements:", numbers[-2:])
    print("Reversed list:", numbers[::-1])


def loop_through_list():
    """Loop through a list"""
    fruits = ["apple", "banana", "cherry"]

    print("Using for loop:")
    for fruit in fruits:
        print(fruit)


def list_length():
    """Get length of list"""
    numbers = [1, 2, 3, 4, 5]
    print("Length:", len(numbers))


def check_membership():
    """Check if item exists in list"""
    fruits = ["apple", "banana", "cherry"]

    print("Is apple in list?", "apple" in fruits)
    print("Is mango in list?", "mango" in fruits)


def sort_list():
    """Sort a list"""
    numbers = [5, 2, 9, 1, 3]

    numbers.sort()
    print("Sorted list:", numbers)


def main():
    # print("\n--- CREATE LIST ---")
    # create_list()
    #
    # print("\n--- ACCESS ELEMENTS ---")
    # access_elements()
    #
    print("\n--- MODIFY ELEMENTS ---")
    modify_elements()
    #
    # print("\n--- ADD ELEMENTS ---")
    # add_elements()
    #
    # print("\n--- REMOVE ELEMENTS ---")
    # remove_elements()
    #
    # print("\n--- LIST SLICING ---")
    # list_slicing()
    #
    # print("\n--- LOOP THROUGH LIST ---")
    # loop_through_list()
    #
    # print("\n--- LIST LENGTH ---")
    # list_length()
    #
    # print("\n--- CHECK MEMBERSHIP ---")
    # check_membership()
    #
    # print("\n--- SORT LIST ---")
    # sort_list()


if __name__ == "__main__":
    main()