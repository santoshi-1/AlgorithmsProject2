m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateMaxNoOfTrees(m, n, h, grid):
    maxTrees = [[0]*(n+1) for i in range(m+1)]
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if grid[row - 1][col - 1] >= h:
                maxTrees[row][col] += 1
            maxTrees[row][col] += maxTrees[row - 1][col] + \
                maxTrees[row][col - 1] - maxTrees[row - 1][col - 1]
    return maxTrees


def calculateMaxSquarePlot(m, n, h, maxTrees, grid):
    result = []
    result_square_size = 0
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            for k in range(0, min(m, n)):
                top_row, top_col = row, col
                bottom_row, bottom_col = row + k, col + k

                if (bottom_row > m or bottom_col > n):
                    break
                else:
                    totalNoOfTrees = (k + 1) * (k + 1)
                    treesPlotted = maxTrees[bottom_row][bottom_col] - maxTrees[bottom_row][top_col - 1] - \
                        maxTrees[top_row - 1][bottom_col] + \
                        maxTrees[top_row-1][top_col-1]
                    diff = totalNoOfTrees - treesPlotted
                    if diff > 4 or result_square_size >= k + 1:
                        continue
                    else:
                        count = 0
                        if grid[top_row - 1][top_col - 1] < h:
                            count += 1
                        if grid[top_row - 1][bottom_col - 1] < h:
                            count += 1
                        if grid[bottom_row - 1][top_col - 1] < h:
                            count += 1
                        if grid[bottom_row - 1][bottom_col - 1] < h:
                            count += 1

                        if (diff == count and result_square_size < k + 1):
                            result_square_size = k + 1
                            result = [top_row, top_col, bottom_row, bottom_col]

    return result


maxTrees = calculateMaxNoOfTrees(m, n, h, grid)
result = calculateMaxSquarePlot(m, n, h, maxTrees, grid)
print(result)
