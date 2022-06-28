#!/usr/bin/python3
'''prints 0 to 99'''

for item in range(0, 99):
    print("{0:2d}".format(item), end=", ")
print("{}".format(99))
