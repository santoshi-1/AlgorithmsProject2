m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h

Initially we are fixing the row_start, col_start values and from this point we are checking for every possible 
square length of size 1 to min(m, n). This can be done by moving diagonally and checking all the elements in the square.
If we encounter any element with value < h, we break out of the loop and check for next plot.

"""


def calculateMaxSquarePlot(m, n, h):
    result = []
    result_square_size = 0
    is_max_square = False

    for row in range(0, m):
        for col in range(0, n):
            if grid[row][col] >= h:
                curr_square_size = 1
                #traversing through the diagonal
                while row + curr_square_size < m and col + curr_square_size < n and grid[row + curr_square_size][col + curr_square_size] >= h:
                    is_max_square = True
                    #check for every value within the square of length row_col_end
                    for row_col_end in range(0, curr_square_size + 1):
                        if grid[row + curr_square_size][col + row_col_end] < h or grid[row + row_col_end][col + curr_square_size] < h:
                            is_max_square = False
                            break
                    if not is_max_square:
                        break
                    else:
                        if result_square_size < curr_square_size:
                            result_square_size = curr_square_size
                            result = [row + 1, col + 1,
                                      row + curr_square_size + 1, col + curr_square_size + 1]
                        curr_square_size += 1
    return result


result = calculateMaxSquarePlot(m, n, h)
print(result[0], result[1], result[2], result[3])
