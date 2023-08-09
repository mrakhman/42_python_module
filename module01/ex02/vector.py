import copy
# Input validation
def is_valid_column_vector(vector):
    if not isinstance(vector, list) \
    or len(vector) == 0 \
    or not all(isinstance(value, list) and len(value) == 1 and isinstance(value[0], float) for value in vector):
        return False
    return True

def is_valid_row_vector(vector):
    if not isinstance(vector, list) \
    or not isinstance(vector[0], list) \
    or not len(vector) == 1 \
    or len(vector[0]) == 0 \
    or not all(isinstance(value, float) for value in vector[0]):
        return False
    return True

# def is_valid_column_vector_shape(shape):
#     if not isinstance(shape, tuple) \
#     or not len(shape) == 2 \
#     or not shape[1] == 1 \
#     or not all(isinstance(shape, int)):
#         return False
#     return True

# def is_valid_row_vector_shape(shape):
#     if not isinstance(shape, tuple) \
#     or not len(shape) == 2 \
#     or not shape[0] == 1 \
#     or not all(isinstance(shape, int)):
#         return False
#     return True

def get_vector_shape(vector):
    if is_valid_column_vector(vector):
        return (len(vector), 1)
    if is_valid_row_vector(vector):
        return (1, len(vector[0]))
    return False

def can_generate_vector_from_size(size):
    if isinstance(size, int) and size > 0:
        return True
    return False

def can_generate_vector_from_range(range):
    if not isinstance(range, tuple) \
    or not len(range) == 2 \
    or not all(isinstance(value, int)  for value in range) \
    or range[0] > range[1]:
        return False
    return True

def is_valid_vector(vector):
    if is_valid_column_vector(vector) or is_valid_row_vector(vector):
        return True
    return False

def get_vector_size(vector):
    if is_valid_column_vector(vector):
        return len(vector)
    if is_valid_row_vector(vector):
        return len(vector[0])
    return False

# To prevent throwing error in console
def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


class Vector:
    @_guard_
    def __init__(self, values):
        if is_valid_vector(values):
            self.values = values
            self.shape = get_vector_shape(values)
        elif can_generate_vector_from_size(values):
            self.values = [[float(i)] for i in range(values)]
            self.shape = get_vector_shape(self.values)
        elif can_generate_vector_from_range(values):
            self.values = [[float(i)] for i in range(values[0], values[1])]
            self.shape = get_vector_shape(self.values)
        else:
            raise ValueError("Error: Invalid values for Vector")
        
    def __str__(self):
        txt = ("Vector values: " + str(self.values) + "\nVector shape:  " + str(self.shape))
        return txt

    def __repr__(self):
        txt = "Vector" + str(self.values) + "; " + str(self.shape)
        return txt
        
    @_guard_
    def __add__(self, v2):
        """Addition of 2 vectors of the same shape"""
        res = copy.deepcopy(self)
        if isinstance(v2, Vector) and res.shape == v2.shape:
            for i in range(len(res.values)):
                for j in range(len(res.values[0])):
                    res.values[i][j] += v2.values[i][j]
            print('4', self.values)
            return res
        else:
            raise ValueError("Error: invalid vector for add operation")
        
    @_guard_
    def __radd__(self, v2):
        self.__add__(v2)

    @_guard_
    def __sub__(self, v2):
        """Substraction of 2 vectors of the same shape"""
        res = copy.deepcopy(self)
        if isinstance(v2, Vector) and res.shape == v2.shape:
            for i in range(len(res.values)):
                for j in range(len(res.values[0])):
                    res.values[i][j] -= v2.values[i][j]
            return res
        else:
            raise ValueError("Error: invalid vector for sub operation")

    @_guard_
    def __rsub__(self, v2):
        self.__sub__(v2)

    @_guard_
    def __truediv__(self):
        """Division of vector and scalar"""
        pass

    @_guard_
    def __rtruediv__(self):
        raise ArithmeticError("Error: can not divide value by vector")
        
    @_guard_
    def dot(self, vector2):
        v1_shape = get_vector_shape(self.values)
        v2_shape = get_vector_shape(vector2.values)
        if not v1_shape == v2_shape:
            raise ValueError("Error: vectors are invalid or not the same dimention")

        def multiply_two_column_vectors(v1, v2):
            return [v1[i][0] * v2[i][0] for i, _el in enumerate(v1)]
        
        def multiply_two_row_vectors(v1, v2):
            return [v1[0][i] * v2[0][i] for i, _el in enumerate(v1[0])]
        
        list_sum = lambda v: v[0] if len(v) == 1 else v[0] + list_sum(v[1:])
        
        if is_valid_column_vector(self.values) and is_valid_column_vector(vector2.values):
            new_v = multiply_two_column_vectors(self.values, vector2.values)
            return list_sum(new_v)
        if is_valid_row_vector(self.values) and is_valid_row_vector(vector2.values):
            new_v = multiply_two_row_vectors(self.values, vector2.values)
            return list_sum(new_v)
        raise ValueError("Error: one or both vectors are invalidd")

    @_guard_
    def T(self):
        if is_valid_column_vector(self.values):
            new_row_v = [[]]
            for el in self.values:
                new_row_v[0].append(el[0])
            return Vector(new_row_v)

        if is_valid_row_vector(self.values):
            new_col_v = []
            for el in self.values[0]:
                new_col_v.append([el])
            return Vector(new_col_v)
        
        raise ValueError("Error: vector can not be transposed")


        
if __name__ == '__main__':
    # pass

    # print(Vector([[1.], [2.], [3.]]).shape)
    # print(Vector([[[1], [2.], [3.]]])) # not valid
    # print(Vector([[[1., 1., 1.], [2., 2., 2.], [3., 3., 3.]]])) # not valid
    # print()
    # print(Vector([[1., 2., 3.]]).shape)
    # print(Vector([[1., 2., 3.], [1., 2., 3.]])) # not valid
    # print(Vector([1., 2., 3.])) # not valid

    # v1 = Vector([[1.], [2.], [3.]])

    v2 = Vector(3) # generate vector from value
    print(v2.shape, v2.values)

    v3 = Vector((0, 3)) # generate vector from range
    print(v3.shape, v3.values)

    print('column dot:', v2.dot(v3))

    v4 = Vector([[0., 1., 2.]])
    v5 = Vector([[0., 1., 2.]])
    v6wrong = Vector([[1.], [2.], [3.]])
    print('row dot:', v4.dot(v5))
    print('row dot:', v4.dot(v6wrong))
