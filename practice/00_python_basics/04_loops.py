# loops

def for_loop_basic():
    """Basic for loop"""
    print("Numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)


def for_loop_list():
    """Loop through a list"""
    fruits = ["apple", "banana", "cherry"]

    print("Fruits:")
    for fruit in fruits:
        print(fruit)


def for_loop_with_index():
    """Loop with index using enumerate"""
    fruits = ["apple", "banana", "cherry"]

    print("Fruits with index:")
    for index, fruit in enumerate(fruits):
        print(index, fruit)


def nested_loops():
    """Nested loops example"""
    print("Multiplication table (1–3):")

    for i in range(1, 4):
        for j in range(1, 4):
            print(i * j, end=" ")
        print()  # new line


def while_loop_basic():
    """Basic while loop"""
    count = 1

    print("While loop from 1 to 5:")
    while count <= 5:
        print(count)
        count += 1


def break_example():
    """Using break to exit loop"""
    print("Break example:")

    for i in range(1, 10):
        if i == 5:
            break
        print(i)


def continue_example():
    """Using continue to skip iteration"""
    print("Continue example:")

    for i in range(1, 6):
        if i == 3:
            continue
        print(i)


def pass_example():
    """Using pass (placeholder)"""
    print("Pass example:")

    for i in range(3):
        pass  # does nothing

    print("Loop completed using pass")


def loop_else():
    """Using else with loops"""
    print("Loop with else:")

    for i in range(3):
        print(i)
    else:
        print("Loop finished successfully")


def sum_example():
    """Sum numbers using loop"""
    total = 0

    for i in range(1, 6):
        total += i

    print("Sum from 1 to 5:", total)


def user_input_example():
    """Simple user input loop"""
    print("Enter 'exit' to stop")

    while True:
        user_input = input("Type something: ")

        if user_input.lower() == "exit":
            break

        print("You typed:", user_input)


def main():
    print("\n--- FOR LOOP BASIC ---")
    for_loop_basic()

    print("\n--- FOR LOOP LIST ---")
    for_loop_list()

    print("\n--- FOR LOOP WITH INDEX ---")
    for_loop_with_index()

    print("\n--- NESTED LOOPS ---")
    nested_loops()

    print("\n--- WHILE LOOP ---")
    while_loop_basic()

    print("\n--- BREAK ---")
    break_example()

    print("\n--- CONTINUE ---")
    continue_example()

    print("\n--- PASS ---")
    pass_example()

    print("\n--- LOOP ELSE ---")
    loop_else()

    print("\n--- SUM EXAMPLE ---")
    sum_example()

    print("\n--- USER INPUT LOOP ---")
    user_input_example()


if __name__ == "__main__":
    main()