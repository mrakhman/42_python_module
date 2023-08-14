from vector import Vector
import unittest


class TestVector(unittest.TestCase):
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

    def test_transpose(self):
        vector1 = Vector([[0., 1., 2.]])
        vector2 = Vector([[0.], [1.], [2.]])

        self.assertEqual(vector1.T().shape, vector2.shape) # row becomes column
        self.assertEqual(vector1.T().T().shape, vector1.shape) # transposing twice returns initial vector
        self.assertEqual(vector2.T().shape, vector1.shape) # column becomes row

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

    def test_mul(self):
        vector1 = Vector([[1., 2., 3.]])
        vector2 = Vector([[1.], [2.], [3.]])
        n1 = 3
        n2 = -3
        n3 = 1.555555
        n4 = 0.0

        self.assertEqual((vector1 * n1).values, [[3., 6., 9.]])
        self.assertEqual((vector2 * n1).values, [[3.], [6.], [9.]])

        self.assertEqual((vector1 * n2).values, [[-3., -6., -9.]])
        self.assertEqual((vector2 * n2).values, [[-3.], [-6.], [-9.]])

        self.assertEqual((vector1 * n3).values, [[1.555555, 3.11111, 4.666665]])
        self.assertEqual((vector2 * n3).values, [[1.555555], [3.11111], [4.666665]])

        self.assertEqual((vector1 * n4).values, [[0.0, 0.0, 0.0]]) # error - not correct vector

    def test_div(self):
        vector1 = Vector([[1., 2., 3.]])
        vector2 = Vector([[1.], [2.], [3.]])
        n1 = 3
        n2 = -3
        n3 = 1.5
        n4 = 0.0

        self.assertEqual((vector1 / n1).values, [[0.33333333, 0.66666667, 1.]])
        self.assertEqual((vector2 / n1).values, [[0.33333333], [0.66666667], [1.]])

        self.assertEqual((vector1 / n2).values, [[-0.33333333, -0.66666667, -1.]])
        self.assertEqual((vector2 / n2).values, [[-0.33333333], [-0.66666667], [-1.]])

        self.assertEqual((vector1 / n3).values, [[0.66666667, 1.33333333, 2.]])
        self.assertEqual((vector2 / n3).values, [[0.66666667], [1.33333333], [2.]])

        self.assertEqual((vector1 / n4), None) # error - division by zero
        self.assertEqual((n1 / vector1), None) # error - division of value by vector


if __name__ == '__main__':
    unittest.main()
