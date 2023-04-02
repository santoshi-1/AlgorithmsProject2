m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateMaxNoOfTrees(m, n, h, grid):
    max_trees = [[0]*(n+1) for i in range(m+1)]
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if grid[row - 1][col - 1] >= h:
                max_trees[row][col] += 1
            max_trees[row][col] += max_trees[row - 1][col] + \
                max_trees[row][col - 1] - max_trees[row - 1][col - 1]
    return max_trees


def calculateMaxSquarePlot(m, n, h, max_trees, grid):
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
                    total_no_of_trees = (k + 1) * (k + 1)
                    trees_plotted = max_trees[bottom_row][bottom_col] - max_trees[bottom_row][top_col - 1] - \
                        max_trees[top_row - 1][bottom_col] + \
                        max_trees[top_row-1][top_col-1]
                    diff = total_no_of_trees - trees_plotted
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


max_trees = calculateMaxNoOfTrees(m, n, h, grid)
result = calculateMaxSquarePlot(m, n, h, max_trees, grid)
print(result)
