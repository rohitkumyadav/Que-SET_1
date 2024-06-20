"""
📌 Description:
Write a Python program that calculates the distance between two 3D points.

The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate.

"""
from math import sqrt

pointA = [3,4,5]
pointB=  [1,3,5]

x1 = pointA[0]
y1 = pointA[1]
z1 = pointA[2]

x2 = pointB[0]
y2 = pointB[1]
z2 = pointB[2]



formula = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

print(f"{formula:.5f}") # f"{number:.2f}"
