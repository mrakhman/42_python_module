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

def is_valid_column_vector_shape(shape):
    if not isinstance(shape, tuple) \
    or not len(shape) == 2 \
    or not shape[1] == 1 \
    or not all(isinstance(shape, int)):
        return False
    return True

def is_valid_row_vector_shape(shape):
    if not isinstance(shape, tuple) \
    or not len(shape) == 2 \
    or not shape[0] == 1 \
    or not all(isinstance(shape, int)):
        return False
    return True

def validate_vector(vector, shape):
    if is_valid_column_vector(vector) and is_valid_column_vector_shape(shape):
        return True
    if is_valid_row_vector(vector) and is_valid_row_vector_shape(shape):
        return True
    return False


class Vector:
    def __init__(self, values, shape):
        if validate_vector(values, shape):
            self.values = values
            self.shape = shape
        else:
            print("Vector is not valid")
            return

### TODO: do I need to check that vector shape and number of valies correspond?

print(Vector([[1.], [2.], [3.]], (1, 4)))
print(Vector([[[1], [2.], [3.]]]))
print()
print(Vector([[1., 2., 3.]]))
print(Vector([[1., 2., 3.], [1., 2., 3.]]))
print(Vector([1., 2., 3.]))
