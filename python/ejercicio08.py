def solution(matrix):
    nueva = []
    suma = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0 and i == 0:
                nueva.append(matrix[i][j])
            elif i == 1 and matrix[i][j] != 0 and matrix[i-1][j] != 0:
                nueva.append(matrix[i][j])
            elif i == 2 and matrix[i][j] != 0 and matrix[i-1][j] != 0 and matrix[i-2][j] != 0:
                nueva.append(matrix[i][j])

    for i in range(len(nueva)):
        suma += nueva[i]

    return suma


matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]


print(solution(matrix))
