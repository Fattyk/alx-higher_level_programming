#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end = number % 10
if (end > 5):
    print(f"Last digit of {number:d} is {end:d} and is greater than 5")
elif (end == 0):
    print(f"Last digit of {number:d} is {end:d} and is 0")
elif ((end < 6) and (end != 0)):
    print(f"Last digit of {number:d} is {end:d} and is less than 6 and not 0")
