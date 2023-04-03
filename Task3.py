m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)

compute_largest_square = [[0]*(n+1) for i in range(m+1)]

""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateMaxSquarePlot(m, n, h):
    result = []
    result_square_size = 0

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if grid[row - 1][col - 1] >= h:
                compute_largest_square[row][col] = min(
                    compute_largest_square[row - 1][col - 1], compute_largest_square[row][col - 1], compute_largest_square[row - 1][col]) + 1

            if result_square_size < compute_largest_square[row][col]:
                result_square_size = compute_largest_square[row][col]
                result = [row - result_square_size + 1,
                          col - result_square_size + 1, row, col]

    return result


result = calculateMaxSquarePlot(m, n, h)
print(result[0], result[1], result[2], result[3])
