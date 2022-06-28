#!/usr/bin/python3
'''prints 0 to 99'''

for item in range(0, 100):
    print("{0:02d}".format(item), sep=", " end="")
print('\n')
