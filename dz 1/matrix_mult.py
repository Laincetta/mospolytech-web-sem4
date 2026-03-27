def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B, n):
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

n = int(input())
A = read_matrix(n)
B = read_matrix(n)
result = multiply_matrices(A, B, n)

print_matrix(result)