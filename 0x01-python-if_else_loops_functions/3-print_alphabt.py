#!/usr/bin/python3
'''program that prints the ASCII alphabet except q and e, in lowercase'''

for item in range(97, 123):
    if chr(item) != 'q' and chr(item) != 'e':
        print("{0:c}".format(item), end="")
