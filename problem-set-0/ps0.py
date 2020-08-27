import numpy as ny

xString = input("Enter number x: ")
yString = input("Enter number y: ")

xInteger = int(xString)
yInteger = int(yString)

print("x**y = ", xInteger ** yInteger)
print("log(x) = ", ny.log2(xInteger))
