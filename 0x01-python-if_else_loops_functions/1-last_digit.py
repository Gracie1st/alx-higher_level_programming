#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
message = ("Last digit of", number,"is", last_digit)
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is zero")
else:
    print("is less than 6 and not 0")
