def print_matrix(matrix):
    """ Print a matrix in a readable format. """
    for row in matrix:
        print([f"{value:.2f}" for value in row])


def swap_rows(matrix, i, j):
    """ Swap rows i and j in a matrix. """
    matrix[i], matrix[j] = matrix[j], matrix[i]

def lu_decomposition(matrix):
    """ Perform LU decomposition with pivoting.
    Returns L (lower triangular matrix), U (upper triangular matrix), and P (permutation matrix). """
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [row[:] for row in matrix]  # Create a copy of the input matrix
    P = [[float(i == j) for j in range(n)] for i in range(n)]

    for j in range(n):
        # Pivot
        max_row = max(range(j, n), key=lambda i: abs(U[i][j]))
        if j != max_row:
            swap_rows(U, j, max_row)
            swap_rows(P, j, max_row)
            swap_rows(L, j, max_row)

        for i in range(j + 1, n):
            pivot = (-U[i][j]) / U[j][j]
            for k in range(n):
                U[i][k] += pivot * U[j][k]
            L[i][j] = -pivot  # שים לב לסימן המינוס כאן

    for i in range(n):
        L[i][i] = 1.0

    return L, U, P


def multiply_matrix(matrix1, matrix2):
    """ Multiply a matrix (matrix1) by a matrix (matrix2). """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Cannot multiply matrices, dimensions do not match.")

    result = [[0.0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def solve_with_lu_decomposition(L, U, P, b):
    """ Solve the linear system Ax = b using LU decomposition and pivoting. """
    n = len(L)
    Pb = multiply_matrix(P, [[b[i]] for i in range(n)])

    # Solve Ly = Pb for y (forward substitution)
    y = [0.0] * n
    for i in range(n):
        y[i] = Pb[i][0]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Solve Ux = y for x (backward substitution)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return [[xi] for xi in x]


def find_inverse(matrix):
    """ Find the inverse of a matrix using LU decomposition and elementary matrices. """
    n = len(matrix)
    L, U, P = lu_decomposition(matrix)
    inverse = []
    for col in range(n):
        b = [float(i == col) for i in range(n)]
        x = solve_with_lu_decomposition(L, U, P, b)
        inverse.append([x[i][0] for i in range(n)])

    # Transpose to get the correct orientation
    inverse = [[inverse[j][i] for j in range(n)] for i in range(n)]
    return inverse


if __name__ == '__main__':
    A = [[1, 4, -3], [-2, 1, 5], [3,2, 1]]
    b = [30, 60, 50]

    # Find the inverse of A
    inverse_A = find_inverse(A)
    print("Inverse matrix A^-1:")
    print_matrix(inverse_A)
    print()

    # Perform LU decomposition of A
    L, U, P = lu_decomposition(A)
    print("Lower triangular matrix L:")
    print_matrix(L)
    print("Upper triangular matrix U:")
    print_matrix(U)
    print("Permutation matrix P:")
    print_matrix(P)
    print()

    # Solve the linear system Ax = b using LU decomposition
    x = solve_with_lu_decomposition(L, U, P, b)
    print("Solution vector x:")
    print_matrix(x)