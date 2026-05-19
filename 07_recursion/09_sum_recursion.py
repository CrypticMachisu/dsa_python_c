def sum(n):

    if n == 1:
        return 1
    return n + sum(n - 1)

res = sum(5)
print(res)

#Expansion

# recursive_sum(5)
# = 5 + recursive_sum(4)
# = 5 + (4 + recursive_sum(3))
# = 5 + (4 + (3 + recursive_sum(2)))
# = 5 + (4 + (3 + (2 + recursive_sum(1))))
# = 5 + (4 + (3 + (2 + 1)))

# Collapse
# recursive_sum(1) = 1
# recursive_sum(2) = 2 + 1 = 3
# recursive_sum(3) = 3 + 3 = 6
# recursive_sum(4) = 4 + 6 = 10
# recursive_sum(5) = 5 + 10 = 15
