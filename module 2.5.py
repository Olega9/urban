def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        key = []
        for j in range(m):
            key.append(value)
        matrix.append(key)
    return matrix
n = 5
m = 3
value = 95

matrix_result = get_matrix(n, m, value)
for key in matrix_result:
    print(key)

