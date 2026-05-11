# set operations in Python

def create_set():
    """Create a simple set"""
    numbers = {1, 2, 3, 4, 5}
    print("Created set:", numbers)


def set_no_duplicates():
    """Sets do not allow duplicates"""
    numbers = {1, 2, 2, 3, 3, 4}
    print("No duplicates:", numbers)


def access_elements():
    """Sets are unordered (no indexing)"""
    fruits = {"apple", "banana", "cherry"}

    print("Set elements (unordered):")
    for fruit in fruits:
        print(fruit)


def add_elements():
    """Add elements to a set"""
    numbers = {1, 2, 3}

    numbers.add(4)
    print("After add:", numbers)

    numbers.update([5, 6])
    print("After update:", numbers)


def remove_elements():
    """Remove elements from a set"""
    numbers = {1, 2, 3, 4}

    numbers.remove(3)  # error if not found
    print("After remove:", numbers)

    numbers.discard(10)  # no error if not found
    print("After discard (no error):", numbers)

    popped = numbers.pop()  # removes random element
    print("Popped element:", popped)
    print("After pop:", numbers)


def set_length():
    """Get length of set"""
    numbers = {1, 2, 3, 4, 5}
    print("Length:", len(numbers))


def check_membership():
    """Check if element exists"""
    fruits = {"apple", "banana", "cherry"}

    print("Is apple in set?", "apple" in fruits)
    print("Is mango in set?", "mango" in fruits)


def union_sets():
    """Union of two sets"""
    a = {1, 2, 3}
    b = {3, 4, 5}

    print("Union using | :", a | b)
    print("Union using union():", a.union(b))


def intersection_sets():
    """Intersection of two sets"""
    a = {1, 2, 3}
    b = {2, 3, 4}

    print("Intersection using &:", a & b)
    print("Intersection using intersection():", a.intersection(b))


def difference_sets():
    """Difference between sets"""
    a = {1, 2, 3}
    b = {2, 3, 4}

    print("A - B:", a - b)
    print("B - A:", b - a)


def symmetric_difference_sets():
    """Symmetric difference (elements not in both)"""
    a = {1, 2, 3}
    b = {3, 4, 5}

    print("Symmetric difference:", a ^ b)


def subset_superset():
    """Check subset and superset"""
    a = {1, 2}
    b = {1, 2, 3, 4}

    print("Is a subset of b?", a.issubset(b))
    print("Is b superset of a?", b.issuperset(a))


def clear_set():
    """Clear all elements"""
    numbers = {1, 2, 3}

    numbers.clear()
    print("After clear:", numbers)


def main():
    print("\n--- CREATE SET ---")
    create_set()

    print("\n--- NO DUPLICATES ---")
    set_no_duplicates()

    print("\n--- ACCESS ELEMENTS ---")
    access_elements()

    print("\n--- ADD ELEMENTS ---")
    add_elements()

    print("\n--- REMOVE ELEMENTS ---")
    remove_elements()

    print("\n--- SET LENGTH ---")
    set_length()

    print("\n--- CHECK MEMBERSHIP ---")
    check_membership()

    print("\n--- UNION ---")
    union_sets()

    print("\n--- INTERSECTION ---")
    intersection_sets()

    print("\n--- DIFFERENCE ---")
    difference_sets()

    print("\n--- SYMMETRIC DIFFERENCE ---")
    symmetric_difference_sets()

    print("\n--- SUBSET & SUPERSET ---")
    subset_superset()

    print("\n--- CLEAR SET ---")
    clear_set()


if __name__ == "__main__":
    main()