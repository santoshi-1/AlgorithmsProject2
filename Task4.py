m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateBinaryMatrix(m, n, h, grid):
    binary_matrix = [[0]*(n) for i in range(m)]
    for row in range(0, m):
        for col in range(0, n):
            if grid[row][col] >= h:
                binary_matrix[row][col] = 1
    return binary_matrix


def formulatePrecomputedMatrix(m, n, binary_matrix):
    precomputed_matrix = [[0]*(n) for i in range(m)]
    for row in range(0, m):
        for col in range(0, n):
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                precomputed_matrix[row][col] = 0
            elif (binary_matrix[row][col] == 1):
                if binary_matrix[row-1][col] == 1 and binary_matrix[row][col-1] == 1 and binary_matrix[row+1][col] == 1 and binary_matrix[row][col+1] == 1:
                    precomputed_matrix[row][col] = precomputed_matrix[row - 1][col] + 1
    return precomputed_matrix


def calculateMaxSquarePlot(m, n, precomputed_matrix):
    result = []
    result_square_size = 0
    col_end = 0
    row_end = 0
    for row in range(0, m):
        for col in range(0, n):
            count = 0
            for i in range(col, n):
                if precomputed_matrix[row][i] >= precomputed_matrix[row][col]:
                    count += 1
                else:
                    break

                if count >= precomputed_matrix[row][col] - 1:
                    if result_square_size <= precomputed_matrix[row][col] + 1:
                        result_square_size = precomputed_matrix[row][col] + 1
                        col_end = i + 2
                        row_end = row + 2
                    break
            count = 0
            for i in range(col, -1, -1):
                if precomputed_matrix[row][i] >= precomputed_matrix[row][col]:
                    count += 1
                else:
                    break
                if count >= precomputed_matrix[row][col] - 1:
                    if result_square_size <= precomputed_matrix[row][col] + 1:
                        result_square_size = precomputed_matrix[row][col] + 1
                        col_end = col + 2
                        row_end = row + 2
                    break

    result = [row_end - result_square_size, col_end -
              result_square_size, row_end, col_end]

    return result


if m == 1 and n == 1:
    print(0, 0, 0, 0)
elif m < 2 and n < 2:
    print(0, 0, 1, 1)
else:
    binary_matrix = calculateBinaryMatrix(m, n, h, grid)
    precomputed_matrix = formulatePrecomputedMatrix(m, n, binary_matrix)
    result = calculateMaxSquarePlot(m, n, precomputed_matrix)
    print(result[0], result[1], result[2], result[3])
