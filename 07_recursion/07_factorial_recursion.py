def factorial(n):

    if n == 0:
        return 1
    return n * factorial(n - 1)

res = factorial(4)
print(res)

# factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * (4 * (3 * (2 * (1 * factorial(0)))))
# = 5 * (4 * (3 * (2 * (1 * 1))))

# factorial(0) = 1
# factorial(1) = 1 * 1 = 1
# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2 = 6
# factorial(4) = 4 * 6 = 24
# factorial(5) = 5 * 24 = 120
