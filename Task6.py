m, n, h, k = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h

At first we are fixing the row_start, col_start values and then we are checking for every possible row_end, col_end values
after we fix the four corners, we are iterating through the matrix from row_start, col_start to row _end and col_end to check
if the square is having all ones with the contraint that it can have upto k zeros. If such square exits and 
its length is greater the max_square_size found so far, we are updating the value

"""


def calculateMaxSquarePlot(m, n, h, k):
    result = []
    result_square_size = 0
    is_max_square = False

    for row_start in range(0, m):
        for col_start in range(0, n):
            for row_end in range(row_start, m):
                for col_end in range(col_start, n):
                    is_max_square = True
                    count = 0
                    for x in range(row_start, row_end + 1):
                        for y in range(col_start, col_end + 1):
                            if grid[x][y] < h and count >= k:
                                is_max_square = False
                                break
                            if grid[x][y] < h:
                                count += 1
                        if not is_max_square:
                            break
                    if is_max_square:
                        if col_end - col_start == row_end - row_start:
                            if result_square_size <= row_end - row_start:
                                result_square_size = row_end - row_start
                                result = [row_start + 1, col_start + 1,
                                          row_end + 1, col_end + 1]
    return result


result = calculateMaxSquarePlot(m, n, h, k)
print(result[0], result[1], result[2], result[3])
