# control_flow

def if_statement():
    """Basic if statement"""
    age = 18

    if age >= 18:
        print("You are an adult")


def if_else_statement():
    """If-else example"""
    number = 7

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def if_elif_else():
    """Multiple conditions"""
    marks = 75

    if marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: D")


def nested_if():
    """Nested if statements"""
    age = 20
    has_id = True

    if age >= 18:
        if has_id:
            print("Allowed entry")
        else:
            print("ID required")
    else:
        print("Too young")


def logical_operators():
    """Using and, or, not"""
    age = 22
    has_id = True

    if age >= 18 and has_id:
        print("Access granted")

    if age < 18 or not has_id:
        print("Access denied condition met")


def comparison_operators():
    """Comparison operators"""
    a = 10
    b = 5

    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)


def ternary_operator():
    """Short-hand if-else"""
    age = 17

    result = "Adult" if age >= 18 else "Minor"
    print("Result:", result)


def match_case_example():
    """Match-case (Python 3.10+)"""
    day = "Monday"

    match day:
        case "Monday":
            print("Start of the week")
        case "Friday":
            print("Almost weekend")
        case "Saturday" | "Sunday":
            print("Weekend")
        case _:
            print("Midweek day")


def try_except_example():
    """Basic error handling"""
    try:
        num = int("abc")  # will cause error
    except ValueError:
        print("Conversion failed")
    finally:
        print("This always runs")


def input_example():
    """Simple user input with control flow"""
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")


def main():
    print("\n--- IF STATEMENT ---")
    if_statement()

    print("\n--- IF ELSE ---")
    if_else_statement()

    print("\n--- IF ELIF ELSE ---")
    if_elif_else()

    print("\n--- NESTED IF ---")
    nested_if()

    print("\n--- LOGICAL OPERATORS ---")
    logical_operators()

    print("\n--- COMPARISON OPERATORS ---")
    comparison_operators()

    print("\n--- TERNARY OPERATOR ---")
    ternary_operator()

    print("\n--- MATCH CASE ---")
    match_case_example()

    print("\n--- TRY EXCEPT ---")
    try_except_example()

    print("\n--- INPUT EXAMPLE ---")
    input_example()


if __name__ == "__main__":
    main()