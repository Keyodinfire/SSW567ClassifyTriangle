'''
By: Andy Molla
Tests the function classify_triangle from the hw_1 module
'''

import unittest
from math import sqrt
from hw_1 import classify_triangle

def run_classify_triangle(side_a, side_b, side_c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classifyTriangle(',side_a, ',', side_b, ',', side_c, ')=',classify_triangle(side_a,side_b,side_c),sep="")

class TestTriangles(unittest.TestCase):
    '''test case class for classify_triangle'''
    def test_set_1(self):
        '''first set of test cases'''
        self.assertEqual(classify_triangle(3,4,5),'Right Scalene','3,4,5 is a Right Scalene triangle')

    def test_my_test_set_2(self):
        '''second set of test cases'''
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isosceles','Should be Equilateral')
        self.assertEqual(classify_triangle(10,21,30),'Scalene','Should be Isoceles')

    def test_my_test_set_3(self):
        '''third set of test cases'''
        self.assertEqual(classify_triangle(10,11,30),'Not a triangle','Should be Not a triangle')
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), 'Right Isosceles', 'Should be Right Isosceles')

if __name__ == '__main__':
    run_classify_triangle(1,2,3)
    run_classify_triangle(1,1,1)
    run_classify_triangle(5, 6, 17)
    run_classify_triangle(10, 15, 20)
    run_classify_triangle(1.1, 1.1, 1.1)
    run_classify_triangle(2.5, 3.7, 5)
    run_classify_triangle(14, 15, 16)
    run_classify_triangle(1.5, 1.5, 2.5)
    run_classify_triangle(8, 8, sqrt(128))
    run_classify_triangle(6, 8, 10)

    unittest.main(exit=True)
