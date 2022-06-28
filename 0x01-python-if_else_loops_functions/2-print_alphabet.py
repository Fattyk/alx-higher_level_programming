#!/usr/bin/python3
'''program that prints the ASCII alphabet, in lowercase'''

for item in range(97, 123):
    print("{0:c}".format(item), end="")
