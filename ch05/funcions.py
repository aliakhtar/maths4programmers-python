from ch05.vectors import *
from random import randint
from numpy import isclose


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for (s, v) in zip(scalars, vectors)]
    return add(*scaled)


def multiply_matrix_vector(matrix, vector):
    if not len(matrix[0]) == len(vector):
        raise Exception("Invalid dimensions, cols in m1 are %d and rows in m2 are %d" % (len(matrix[0]), len(vector)))
    scalars = vector
    vectors = zip(*matrix)
    return linear_combination(scalars, *vectors)


def multiply_matrix(a, b):
    verify_matrix_dimensions(a, b)
    # We'll view a as a list of its row vectors, and a as a list of its column vectors.
    # E.g if a = [
    # (a, b, c)
    # (d, e, f)
    # (g, h, i)  ]
    # then we'll take the rows (i.e (a, b, c), (d, e, f), (g, h, i ) from it.
    # And if b has the same values, we'll take (a, d, g), (b, e, h), and (c, f, i)

    # Then we want to go thru the rows, and for each row, go thru the cols and take their dot prod of the row.col
    # Each resulting value will be a point in the next column in the result.

    # E.g result = [
    # (r1.c1 , r1.c2,  r1.c3),
    # (r2.c1,  r2.c2,  r2.c3),
    # (r3.c1,  r3.c2,  r3.c3) ]
    # In the end we zip the columns together to put them all in the same matrix and return the result.

    # I.e each row in the result matrix is a tuple of all dot products of a particular row w/ all cols

    return tuple(
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )


# Returns a tuple representing the standard basis vector for the given value of i. E.g if i is 1, x will be 1,
# and all other coords until n will be 0.
def standard_basis(i, n):
    return tuple(1 if j == i else 0 for j in range(1, n + 1))


# Given n representing the number of dimensions and T as a function which takes in a vector and performs
# some linear transform on it, this function returns a matrix representing the results of performing T on N
# standard basis vectors.

# If input is a function which scales a vector by 2, and n = 3, the output will be:

# (
#   (2, 0, 0),
#   (0, 2, 0),
#   (0, 0, 2)
# )

# I.e it'll be 3 by 3, 3 rows and 3 columns
def infer_matrix(n, T):
    inputs = [standard_basis(i, n) for i in range(1, n + 1)]
    # print(inputs)
    transformed = tuple(T(i) for i in inputs)
    return tuple(zip(*transformed))


# Returns a matrix of the specified size containing random whole numbers as the values
# Min and max specify the upper and lower bounds on the generated whole numbers
def random_matrix(rows, cols, min=-2, max=2):
    return tuple(
        tuple(randint(min, max) for i in range(cols))
        for j in range(rows)
    )


def matrix_power(power, matrix):
    result = matrix
    for _ in range(1, power):
        result = multiply_matrix(result, matrix)

    return result


def verify_matrix_dimensions(m1, m2):
    # Make sure that the number of cols in m1 are the same as number of rows in m2
    cols_in_m1 = len(m1[0])
    rows_in_m2 = len(m2)

    if (cols_in_m1 != rows_in_m2):
        raise Exception("Invalid matrix dimensions, %d cols in m1 and %d rows in m2" % (cols_in_m1, rows_in_m2))


# Turns a column vector into a row vector or vice versa
# eg if 1 col and 3 rows, returns 1 row with 3 cols, and vice versa.

def transpose(vector):
    return tuple(zip(*vector))


def verify_linear_sum(T, u, v):
    # T(u) + T(v) = T(u + v)
    Tu = T(u)
    Tv = T(v)

    print("u: %s, v: %s, u + v: %s" %( str(u), str(v), str(add(u, v))))
    print("T(u): %s, T(v): %s" % (str(Tu), str(Tv)))
    print("T(u) + T(v): %s" % str(add(Tu, Tv)))
    print("T(u + v): %s" % str( T( add(u, v) ) ))
    print("Equal? %s" % str( isclose( add(Tu, Tv) ,T( add(u, v) ) ).all() ))
    return isclose(add(Tu, Tv), T(add(u, v))).all() == True


def verify_linear_multiples(T, s, v):
    # T(sv) = s(T(v))
    sv = scale(s, v)
    Tv = T(v)
    # return T(sv) == scale(s, Tv)
    return isclose(T(sv), scale(s, Tv)).all() == True
