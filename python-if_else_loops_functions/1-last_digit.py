#!/usr/bin/python3
import random
numb = random.randint(-10000, 10000)
r = abs(numb) % 10
r *= -1 if numb < 0 else 1
if r >5:
    print(f"Last digit of {numb} is {r} and is freater than 5")
elif r == 0:
    print(f"Last digit of {numb} is {r} and is 0")
else:
    print(f"Last digit of {numb} is {r} and is less than 6 and not 0")
