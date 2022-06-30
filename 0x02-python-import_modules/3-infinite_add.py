#!/usr/bin/python3
if __name__ == "__main__":
    """a program that prints the result of the addition of all arguments"""
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("{}".format(0))
    elif argc == 1:
        print("{}".format(sys.argv[1]))
    else:
        sum = 0
        for i in range(argc):
            sum += int(sys.argv[i + 1])
        print("{}".format(sum))
