#!/usr/bin/python3


if __name__ == "__main__":
    """Import and print addition such that 1 + 2 = 3"""
    from add_0 import add
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}\n".format(a, b, add(a, b)))
