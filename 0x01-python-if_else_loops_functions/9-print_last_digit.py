#!/usr/bin/python3
'''a function that prints the last digit of a number'''


def print_last_digit(number):
    '''Function that prints last digit'''
    if number < 0:
        sign = -1
        number *= sign
    else:
        sign = 1
    end = (number % 10)
    end *= sign
    print(end)
    return end
