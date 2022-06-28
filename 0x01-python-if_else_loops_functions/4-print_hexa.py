#!/usr/bin/python3
'''prints 0 to 98 in decimal and in hexadecimal'''

for item in range(0, 99):
    print("{0:d} = 0x{0:x}".format(item))
