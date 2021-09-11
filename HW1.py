#By: Andy Molla
import unittest
from math import sqrt
from math import isclose

def classify_triangle(a, b, c):
    '''Determines if the dimensions input into the function can be a valid triangle and determines the type of triangle'''
    triangle = ""

    if a + b > c and a + c > b and b + c > a:
        if a**2 + b**2 == c**2 or isclose(a**2 + b**2, c**2, abs_tol=1e-18):
            triangle = triangle + "Right "
        if a == b == c:
            triangle = triangle + "Equilateral"
        elif a == b or a == c or b == c:
            triangle = triangle + "Isosceles"
        elif a != b != c:
            triangle = triangle + "Scalene"
    else:
        triangle = triangle + "Not a triangle"
        
    return triangle