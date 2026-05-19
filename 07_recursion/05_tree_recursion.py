def tree_recursion(n):
    """Function makes multiple recursive calls"""
    if n <= 0:
        return
    print("Tree:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)

tree_recursion(5)