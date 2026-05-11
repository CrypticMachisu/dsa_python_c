# tuple operations in Python

def create_tuple():
    """Create a simple tuple"""
    numbers = (1, 2, 3, 4, 5)
    print("Created tuple:", numbers)


def access_elements():
    """Access elements using index"""
    fruits = ("apple", "banana", "cherry")

    print("First element:", fruits[0])
    print("Last element:", fruits[-1])


def tuple_length():
    """Get length of tuple"""
    numbers = (1, 2, 3, 4, 5)
    print("Length:", len(numbers))


def single_element_tuple():
    """Create a tuple with one element"""
    single = (5,)  # NOTE the comma!
    print("Single element tuple:", single)


def tuple_slicing():
    """Demonstrate slicing"""
    numbers = (1, 2, 3, 4, 5)

    print("First 3 elements:", numbers[:3])
    print("Last 2 elements:", numbers[-2:])
    print("Reversed tuple:", numbers[::-1])


def loop_tuple():
    """Loop through a tuple"""
    fruits = ("apple", "banana", "cherry")

    for fruit in fruits:
        print(fruit)


def check_membership():
    """Check if item exists in tuple"""
    fruits = ("apple", "banana", "cherry")

    print("Is apple in tuple?", "apple" in fruits)
    print("Is mango in tuple?", "mango" in fruits)


def count_and_index():
    """Use count() and index()"""
    numbers = (1, 2, 2, 3, 4)

    print("Count of 2:", numbers.count(2))
    print("Index of 3:", numbers.index(3))


def convert_tuple_list():
    """Convert between tuple and list"""
    numbers = (1, 2, 3)

    numbers_list = list(numbers)
    print("Tuple to list:", numbers_list)

    numbers_list.append(4)

    numbers_tuple = tuple(numbers_list)
    print("List back to tuple:", numbers_tuple)


def unpack_tuple():
    """Unpack tuple into variables"""
    person = ("Kelvin", 20, "Kenya")

    name, age, country = person
    print("Name:", name)
    print("Age:", age)
    print("Country:", country)


def nested_tuple():
    """Example of nested tuple"""
    nested = ((1, 2), (3, 4), (5, 6))

    print("Nested tuple:", nested)
    print("Access inner element:", nested[1][0])  # 3


def tuple_immutability():
    """Demonstrate immutability"""
    numbers = (1, 2, 3)

    # numbers[0] = 10  # This will cause an error
    print("Tuples are immutable (cannot be changed directly)")


def main():
    print("\n--- CREATE TUPLE ---")
    create_tuple()

    print("\n--- ACCESS ELEMENTS ---")
    access_elements()

    print("\n--- TUPLE LENGTH ---")
    tuple_length()

    print("\n--- SINGLE ELEMENT TUPLE ---")
    single_element_tuple()

    print("\n--- TUPLE SLICING ---")
    tuple_slicing()

    print("\n--- LOOP TUPLE ---")
    loop_tuple()

    print("\n--- CHECK MEMBERSHIP ---")
    check_membership()

    print("\n--- COUNT AND INDEX ---")
    count_and_index()

    print("\n--- CONVERT TUPLE & LIST ---")
    convert_tuple_list()

    print("\n--- UNPACK TUPLE ---")
    unpack_tuple()

    print("\n--- NESTED TUPLE ---")
    nested_tuple()

    print("\n--- TUPLE IMMUTABILITY ---")
    tuple_immutability()


if __name__ == "__main__":
    main()