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
                if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                    binary_matrix[row][col] = 0
                else:
                    if grid[row-1][col] >= h and grid[row+1][col] >= h and grid[row][col-1] >= h and grid[row][col+1] >= h:
                        binary_matrix[row][col] = 1
    return binary_matrix


def formulatePrecomputedMatrix(row, col, binary_matrix, opt, m, n):
    # base case
    if row == m or col == n or binary_matrix[row][col] == 0:
        return 0

    # check memoization table
    elif opt[row][col] != -1:
        return opt[row][col]

    # recursive case
    right = formulatePrecomputedMatrix(row, col + 1, binary_matrix, opt, m, n)
    below = formulatePrecomputedMatrix(row + 1, col, binary_matrix, opt, m, n)
    diagonal = formulatePrecomputedMatrix(
        row + 1, col + 1, binary_matrix, opt, m, n)

    size = 1 + min(right, below, diagonal)
    opt[row][col] = size

    return size


if m == 1 and n == 1:
    print(0, 0, 0, 0)
elif m < 2 and n < 2:
    print(0, 0, 1, 1)
else:
    binary_matrix = calculateBinaryMatrix(m, n, h, grid)
    opt = [[-1]*(n) for i in range(m)]
    max_size = 0
    result_row = result_col = 0
    for i in range(0, m):
        for j in range(0, n):
            if opt[i][j] == -1:
                opt[i][j] = formulatePrecomputedMatrix(
                    i, j, binary_matrix, opt, m-1, n-1)
                if (opt[i][j] > max_size):
                    result_row = i
                    result_col = j
                    max_size = opt[i][j]

    result = [result_row, result_col, result_row +
              max_size + 1, result_col + max_size + 1]

    print(result[0], result[1], result[2], result[3])
