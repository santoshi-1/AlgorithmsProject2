m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateMaxSquarePlot(m, n, h):
    result = []
    result_square_size = 0
    is_max_square = False

    for row_start in range(0, m):
        for col_start in range(0, n):
            for row_end in range(row_start, m):
                for col_end in range(col_start, n):
                    is_max_square = True
                    for x in range(row_start, row_end + 1):
                        for y in range(col_start, col_end + 1):
                            if grid[x][y] < h:
                                is_max_square = False
                                break
                        if not is_max_square:
                            break
                    if is_max_square:
                        if col_end - col_start == row_end - row_start:
                            if result_square_size <= row_end - row_start:
                                result_square_size = row_end - row_start
                                result = [row_start + 1, col_start + 1,
                                          row_end + 1, col_end + 1]
    return result


result = calculateMaxSquarePlot(m, n, h)
print(result)
