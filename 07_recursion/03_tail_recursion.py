def tail_recursion(n):
    if n < 1:
        return n

    print(n)
    return tail_recursion(n - 1)

tail_recursion(5)