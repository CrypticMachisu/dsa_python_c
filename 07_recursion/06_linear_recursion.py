def linear_recursion(n):
    """Only ONE recursive call per function call"""
    if n == 0:
        return
    print("Linear:", n)
    linear_recursion(n - 1)

linear_recursion(5)