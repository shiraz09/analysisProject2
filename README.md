# README

## LU Decomposition and Matrix Operations

This Python script provides a collection of functions to perform LU decomposition with pivoting and various matrix operations, including finding the inverse of a matrix and solving a linear system using LU decomposition. The script includes the following functions:

1. `print_matrix(matrix)`: Prints a matrix in a readable format.
2. `swap_rows(matrix, i, j)`: Swaps rows `i` and `j` in a matrix.
3. `lu_decomposition(matrix)`: Performs LU decomposition with pivoting. Returns the lower triangular matrix `L`, upper triangular matrix `U`, and permutation matrix `P`.
4. `multiply_matrix(matrix1, matrix2)`: Multiplies two matrices.
5. `solve_with_lu_decomposition(L, U, P, b)`: Solves the linear system `Ax = b` using LU decomposition and pivoting.
6. `find_inverse(matrix)`: Finds the inverse of a matrix using LU decomposition.

### Usage

The script includes a `main` block that demonstrates the functionality of the provided functions.

1. **Find the Inverse of a Matrix:**
   ```python
   A = [[1, 4, -3], [-2, 1, 5], [3, 2, 1]]
   inverse_A = find_inverse(A)
   print("Inverse matrix A^-1:")
   print_matrix(inverse_A)
   ```

2. **Perform LU Decomposition:**
   ```python
   L, U, P = lu_decomposition(A)
   print("Lower triangular matrix L:")
   print_matrix(L)
   print("Upper triangular matrix U:")
   print_matrix(U)
   print("Permutation matrix P:")
   print_matrix(P)
   ```

3. **Solve a Linear System:**
   ```python
   b = [30, 60, 50]
   x = solve_with_lu_decomposition(L, U, P, b)
   print("Solution vector x:")
   print_matrix(x)
   ```

### Functions

#### `print_matrix(matrix)`
Prints a matrix in a readable format.

**Parameters:**
- `matrix`: List of lists representing the matrix.

#### `swap_rows(matrix, i, j)`
Swaps rows `i` and `j` in a matrix.

**Parameters:**
- `matrix`: List of lists representing the matrix.
- `i`: Index of the first row.
- `j`: Index of the second row.

#### `lu_decomposition(matrix)`
Performs LU decomposition with pivoting. Returns the lower triangular matrix `L`, upper triangular matrix `U`, and permutation matrix `P`.

**Parameters:**
- `matrix`: List of lists representing the matrix to decompose.


    x = solve_with_lu_decomposition(L, U, P, b)
    print("Solution vector x:")
    print_matrix(x)
```

This script can be run directly to see the output of the various matrix operations and LU decomposition.
