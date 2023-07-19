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
    return None

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


class Vector:
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
        
    def dot(self, vector2):
        v1_shape = get_vector_shape(self)
        v2_shape = get_vector_shape(vector2)
        if not v1_shape == v2_shape:
            raise ValueError("Error: one or both vectors are invalid")

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
        return print("Error: one or both vectors are invalidd")

        


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
print('row dot:', v4.dot(v5))
