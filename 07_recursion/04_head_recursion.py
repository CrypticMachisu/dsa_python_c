def head_recursion(n):
    if n < 1:
        return n

    head_recursion(n - 1)
    print(n)


head_recursion(5)