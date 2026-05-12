def a():
    print(f"1")
    b()
    print(f"2")

def b():
    print(f"3")
    c()
    print(f"4")

def c():
    print(f"5")
    return 0

a() # start

