def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not suitable for multiplication")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
matrix_A = [[1, 2, 3], [4, 5, 6]]
matrix_B = [[7, 8], [9, 10], [11, 12]]
output = matrix_multiply(matrix_A, matrix_B)
print(output)