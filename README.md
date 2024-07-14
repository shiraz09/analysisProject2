# LU Decomposition and Matrix Operations

This Python script provides a collection of functions to perform LU decomposition with pivoting and various matrix operations, including finding the inverse of a matrix and solving a linear system using LU decomposition.

## Functions

### `print_matrix(matrix)`
Prints a matrix in a readable format.

**Parameters:**
- `matrix`: List of lists representing the matrix.

### `swap_rows(matrix, i, j)`
Swaps rows `i` and `j` in a matrix.

**Parameters:**
- `matrix`: List of lists representing the matrix.
- `i`: Index of the first row.
- `j`: Index of the second row.

### `lu_decomposition(matrix)`
Performs LU decomposition with pivoting. Returns the lower triangular matrix `L`, upper triangular matrix `U`, and permutation matrix `P`.

**Parameters:**
- `matrix`: List of lists representing the matrix to decompose.

**Returns:**
- `L`: Lower triangular matrix.
- `U`: Upper triangular matrix.
- `P`: Permutation matrix.

### `multiply_matrix(matrix1, matrix2)`
Multiplies two matrices.

**Parameters:**
- `matrix1`: First matrix.
- `matrix2`: Second matrix.

**Returns:**
- `result`: Product of the two matrices.

### `solve_with_lu_decomposition(L, U, P, b)`
Solves the linear system `Ax = b` using LU decomposition and pivoting.

**Parameters:**
- `L`: Lower triangular matrix.
- `U`: Upper triangular matrix.
- `P`: Permutation matrix.
- `b`: Right-hand side vector.

**Returns:**
- `x`: Solution vector.

### `find_inverse(matrix)`
Finds the inverse of a matrix using LU decomposition.

**Parameters:**
- `matrix`: Matrix to invert.

**Returns:**
- `inverse`: Inverse of the matrix.

## Usage

The script includes a `main` block that demonstrates the functionality of the provided functions.

### Example

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

### Full Example Code

```python
if __name__ == '__main__':
    A = [[1, 4, -3], [-2, 1, 5], [3, 2, 1]]
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
```

This script can be run directly to see the output of the various matrix operations and LU decomposition.
