#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_str = []
        for i in my_string:
            if i not in ['C', 'c']:
                my_str.append(i)
        my_string = ''.join(my_str)
    return my_string
