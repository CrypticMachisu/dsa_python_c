# functions

def basic_function():
    """A simple function"""
    print("Hello, this is a function")


def function_with_parameters(name):
    """Function with one parameter"""
    print("Hello,", name)


def function_with_multiple_parameters(name, age):
    """Function with multiple parameters"""
    print(f"{name} is {age} years old")


def function_with_return():
    """Function that returns a value"""
    return 10 + 5


def function_with_return_parameters(a, b):
    """Function with parameters and return value"""
    return a + b


def default_parameters(name="Student"):
    """Function with default parameter"""
    print("Hello,", name)


def keyword_arguments(name, age):
    """Using keyword arguments"""
    print(f"{name} is {age} years old")


def arbitrary_arguments(*args):
    """Function with arbitrary arguments"""
    print("Values:", args)

    for value in args:
        print(value)


def arbitrary_keyword_arguments(**kwargs):
    """Function with arbitrary keyword arguments"""
    print("Key-Value pairs:", kwargs)

    for key, value in kwargs.items():
        print(key, ":", value)


def lambda_function():
    """Simple lambda function"""
    add = lambda a, b: a + b
    print("Lambda result:", add(3, 4))


def recursion_example(n):
    """Recursion example: factorial"""
    if n == 1:
        return 1
    return n * recursion_example(n - 1)


def docstring_example():
    """This function demonstrates a docstring"""
    print("Check the docstring using help()")


def main():
    print("\n--- BASIC FUNCTION ---")
    basic_function()

    print("\n--- FUNCTION WITH PARAMETER ---")
    function_with_parameters("Kelvin")

    print("\n--- MULTIPLE PARAMETERS ---")
    function_with_multiple_parameters("Kelvin", 20)

    print("\n--- FUNCTION WITH RETURN ---")
    result = function_with_return()
    print("Returned value:", result)

    print("\n--- RETURN WITH PARAMETERS ---")
    print("Sum:", function_with_return_parameters(5, 7))

    print("\n--- DEFAULT PARAMETERS ---")
    default_parameters()
    default_parameters("Alice")

    print("\n--- KEYWORD ARGUMENTS ---")
    keyword_arguments(age=25, name="Bob")

    print("\n--- *ARGS ---")
    arbitrary_arguments(1, 2, 3, 4)

    print("\n--- **KWARGS ---")
    arbitrary_keyword_arguments(name="Alice", age=21, country="Kenya")

    print("\n--- LAMBDA FUNCTION ---")
    lambda_function()

    print("\n--- RECURSION ---")
    print("Factorial of 5:", recursion_example(5))

    print("\n--- DOCSTRING ---")
    docstring_example()


if __name__ == "__main__":
    main()