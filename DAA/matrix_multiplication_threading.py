import threading

def multiply_row(row_index, A, B, result):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[row_index][j] += A[row_index][k] * B[k][j]

def multithreaded_matrix_multiply_row(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not suitable for multiplication")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    threads = []
    for i in range(len(A)):
        thread = threading.Thread(target=multiply_row, args=(i, A, B, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

def multiply_cell(i, j, A, B, result):
    for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]

def multithreaded_matrix_multiply_cell(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not suitable for multiplication")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    threads = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=multiply_cell, args=(i, j, A, B, result))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result

# Example usage:

matrix_A = [[1, 2, 3], [4, 5, 6]]
matrix_B = [[7, 8], [9, 10], [11, 12]]
output1 = multithreaded_matrix_multiply_row(matrix_A, matrix_B)
output2 = multithreaded_matrix_multiply_cell(matrix_A, matrix_B)
print(output1)
print(output2)