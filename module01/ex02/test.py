from vector import Vector
import unittest
import numpy as np


class TestVector(unittest.TestCase):
    @unittest.skip # TODO: rm
    def test_dot_product(self):
        # Row vector
        vector1 = Vector([[0., 1., 2.]])
        vector2 = Vector([[0., 1., 2.]])

        self.assertEqual(vector1.dot(vector2), 5.0)
        self.assertEqual(vector1.dot(Vector([[0., 1., 2., 3.]])), None) # error - different size
        self.assertEqual(vector1.dot(Vector([[0.], [1.], [2.]])), None) # error - different shape

        # Column vector
        vector3 = Vector([[0.], [1.], [2.]])
        vector4 = Vector([[0.], [1.], [2.]])

        self.assertEqual(vector3.dot(vector4), 5.0)
        self.assertEqual(vector3.dot(Vector([[0.], [1.], [2.], [3.]])), None) # error - different size
        self.assertEqual(vector3.dot(Vector([[0., 1., 2.]])), None) # error - different shape

    @unittest.skip # TODO: rm
    def test_transpose(self):
        vector1 = Vector([[0., 1., 2.]])
        vector2 = Vector([[0.], [1.], [2.]])

        self.assertEqual(vector1.T().shape, vector2.shape) # row becomes column
        self.assertEqual(vector1.T().T().shape, vector1.shape) # transposing twice returns initial vector
        self.assertEqual(vector2.T().shape, vector1.shape) # column becomes row

    # @unittest.skip # TODO: rm
    def test_add(self):
        vector1 = Vector([[0., 1., 2.]])
        vector2 = Vector([[0., 1., 2.]])
        vector3 = Vector([[0., 1., 2., 3., 4.]])
        vector4 = Vector([[0.], [1.], [2.]])
        vector5 = Vector([[0.], [1.], [2.]])

        self.assertEqual((vector1 + vector2).values, [[0., 2., 4.]])
        self.assertEqual((vector4 + vector5).values, [[0.], [2.], [4.]])
        self.assertEqual([1., 3., 0.] + vector2, None) # error - first argument not a Vector
        self.assertEqual(vector2 + vector3, None) # error - different shapes
    
    def test_sub(self):
        vector1 = Vector([[0., 1., 2.]])
        vector2 = Vector([[0., 2., 6.]])
        vector3 = Vector([[0., 1., 2., 3., 4.]])
        vector4 = Vector([[0.], [1.], [2.]])
        vector5 = Vector([[3.], [4.], [5.]])


        self.assertEqual((vector1 - vector2).values, [[0., -1., -4.]])
        self.assertEqual((vector4 - vector5).values, [[-3.], [-3.], [-3.]])
        self.assertEqual([1., 3., 0.] - vector2, None) # error - first argument not a Vector
        self.assertEqual(vector2 - vector3, None) # error - different shapes

        print()
        print('asasas', vector1.values)
        print('asasas', vector4.values)
        
        

    

if __name__ == '__main__':
    unittest.main()
    a = np.array([[1.], [2.], [3.]])
    b = np.array([[1.], [8.], [6.]])
    print(a - b)
    print()
    print(a)
    print()

    print(b)
    # b = np.array([[1., 2., 3.]])
    # d = np.array([[1., 2., 3.]])
    # c = b + b
    # print(c)
    # print(a)
    # print()
    # print(np.transpose(a))
    # print()
    # print(a)

    # print(np.transpose(b))
