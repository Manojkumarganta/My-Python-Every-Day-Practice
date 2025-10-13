# Program to find roots of a quadratic equation

import math

# coefficients a, b and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# check the nature of the roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two distinct real roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2*a)
    print("Two equal real roots:")
    print("Root =", root)

else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-d) / (2*a)
    print("Complex roots:")
    print(f"Root 1 = {realPart} + {imagPart}i")
    print(f"Root 2 = {realPart} - {imagPart}i")
