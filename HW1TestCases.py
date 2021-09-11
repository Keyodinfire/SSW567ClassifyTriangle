import unittest
from math import sqrt
from math import isclose
from HW1 import *

def runClassifyTriangle(a, b, c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classify_triangle(3,4,5),'Right Scalene','3,4,5 is a Right Scalene triangle')
        
    def testMyTestSet2(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isosceles','Should be Equilateral')
        self.assertEqual(classify_triangle(10,21,30),'Scalene','Should be Isoceles')
    
    def testMyTestSet3(self): 
        self.assertEqual(classify_triangle(10,11,30),'Not a triangle','Should be Not a triangle')
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), 'Right Isosceles', 'Should be Right Isosceles')

if __name__ == '__main__':
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(5, 6, 17)
    runClassifyTriangle(10, 15, 20)
    runClassifyTriangle(1.1, 1.1, 1.1)
    runClassifyTriangle(2.5, 3.7, 5)
    runClassifyTriangle(14, 15, 16)
    runClassifyTriangle(1.5, 1.5, 2.5)
    runClassifyTriangle(8, 8, sqrt(128))
    runClassifyTriangle(6, 8, 10)
    
    unittest.main(exit=True)