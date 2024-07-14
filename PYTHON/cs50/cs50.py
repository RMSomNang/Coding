# Strip = remove white space
# Capitalize, Title

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getName():
    name = input("What's your name? ").strip().title()
    return name
def getAge():
    age = input("How old are you? ").strip()
    return age

# Name = getName()
# Age = getAge()

# FullName = Name.split(",")

# print(FullName)
# print(f"Hello, my name is {FullName[0]} and I am {Age} years old.")

def sum():
    x = float(input("What's is X? "))
    y = float(input("What's Y? "))
    return round(x + y)

def divide():
    x = float(input("What's is X? "))
    y = float(input("What's is Y? "))
    return x/y

z = divide()

# print(f"The sum of X and Y is: {sum():,}.")
print(f"The division of X and Y is: {z:.2f}.")