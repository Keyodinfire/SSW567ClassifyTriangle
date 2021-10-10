'''
By: Andy Molla
This module takes input in the form of three sides of a potential triangle and checks if they are
a valid triangle a classifies the triangle
'''
from math import isclose

def classify_triangle(side_a, side_b, side_c):
    '''Determines if the dimensions input into the function can be a
    valid triangle and determines the type of triangle'''
    triangle = ""
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        if side_a**2 + side_b**2 == side_c**2 or isclose(side_a**2 + side_b**2, side_c**2, abs_tol=1e-18) or side_a**2 + side_c**2 == side_b**2 or isclose(side_a**2 + side_c**2, side_b**2, abs_tol=1e-18) or side_c**2 + side_b**2 == side_a**2 or isclose(side_c**2 + side_b**2, side_a**2, abs_tol=1e-18):
            triangle = triangle + "Right "
        if side_a == side_b == side_c:
            triangle = triangle + "Equilateral"
        elif side_a == side_b or side_a == side_c or side_b == side_c:
            triangle = triangle + "Isosceles"
        elif side_a != side_b != side_c:
            triangle = triangle + "Scalene"
    else:
        triangle = triangle + "Not a triangle"

    return triangle
