# basic dictionary operations in Python

def create_dictionary():
    """Create a simple dictionary"""
    student = {
        "name": "Kelvin",
        "age": 20,
        "course": "Computer Science"
    }
    print("Created dictionary:", student)


def access_values():
    """Access values using keys"""
    student = {
        "name": "Kelvin",
        "age": 20,
        "course": "Computer Science"
    }

    print("Name:", student["name"])
    print("Age:", student.get("age"))  # safer method


def modify_values():
    """Modify dictionary values"""
    student = {
        "name": "Kelvin",
        "age": 20
    }

    print("Before Modification:", student)
    student["age"] = 21
    print("Modified dictionary:", student)


def add_items():
    """Add new key-value pairs"""
    student = {
        "name": "Kelvin",
        "age": 20
    }

    student["course"] = "Computer Science"
    print("After adding:", student)


def remove_items():
    """Remove items from dictionary"""
    student = {
        "name": "Kelvin",
        "age": 20,
        "course": "Computer Science"
    }

    student.pop("age")  # remove by key
    print("After pop:", student)

    student.popitem()  # removes last inserted item
    print("After popitem:", student)


def dictionary_length():
    """Get number of key-value pairs"""
    student = {
        "name": "Kelvin",
        "age": 20,
        "course": "Computer Science"
    }

    print("Length:", len(student))


def check_key_exists():
    """Check if a key exists"""
    student = {
        "name": "Kelvin",
        "age": 20
    }

    print("Is 'name' a key?", "name" in student)
    print("Is 'course' a key?", "course" in student)


def loop_dictionary():
    """Loop through dictionary"""
    student = {
        "name": "Kelvin",
        "age": 20,
        "course": "Computer Science"
    }

    print("Keys:")
    for key in student:
        print(key)

    print("\nValues:")
    for value in student.values():
        print(value)

    print("\nKey-Value pairs:")
    for key, value in student.items():
        print(key, ":", value)


def copy_dictionary():
    """Copy a dictionary"""
    student = {
        "name": "Kelvin",
        "age": 20
    }

    new_student = student.copy()
    print("Copied dictionary:", new_student)


def clear_dictionary():
    """Clear all items"""
    student = {
        "name": "Kelvin",
        "age": 20
    }

    student.clear()
    print("After clear:", student)


def nested_dictionary():
    """Example of nested dictionary"""
    students = {
        "student1": {"name": "Alice", "age": 21},
        "student2": {"name": "Bob", "age": 22}
    }

    print("Nested dictionary:", students)
    print("Access nested value:", students["student1"]["name"])


def main():
    print("\n--- CREATE DICTIONARY ---")
    create_dictionary()

    print("\n--- ACCESS VALUES ---")
    access_values()

    print("\n--- MODIFY VALUES ---")
    modify_values()

    print("\n--- ADD ITEMS ---")
    add_items()

    print("\n--- REMOVE ITEMS ---")
    remove_items()

    print("\n--- DICTIONARY LENGTH ---")
    dictionary_length()

    print("\n--- CHECK KEY EXISTS ---")
    check_key_exists()

    print("\n--- LOOP DICTIONARY ---")
    loop_dictionary()

    print("\n--- COPY DICTIONARY ---")
    copy_dictionary()

    print("\n--- CLEAR DICTIONARY ---")
    clear_dictionary()

    print("\n--- NESTED DICTIONARY ---")
    nested_dictionary()


if __name__ == "__main__":
    main()