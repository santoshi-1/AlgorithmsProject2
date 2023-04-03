m, n, h, k = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


"""compute the pre computed matrix where each contains the count of all the one's until that cell from the cell (0,0).
"""


def calculateMaxNoOfTrees(m, n, h, grid):
    valid_tree_cells = [[0]*(n+1) for i in range(m+1)]
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if grid[row - 1][col - 1] >= h:
                valid_tree_cells[row][col] += 1
            valid_tree_cells[row][col] += valid_tree_cells[row - 1][col] + \
                valid_tree_cells[row][col - 1] - \
                valid_tree_cells[row - 1][col - 1]
    return valid_tree_cells


"""Using the precomputed matrix, for every possible square length find the number of invalid cells with plot having tree < h.
    for every such possible square, it can be done in O(1) time. Using these invalid cells, we can compute the possible largest square.
 """


def calculateMaxSquarePlot(m, n, h, k, valid_tree_cells, grid):
    result = []
    result_square_size = 0
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            for l in range(0, min(m, n)):
                top_row, top_col = row, col
                bottom_row, bottom_col = row + l, col + l

                if (bottom_row > m or bottom_col > n):
                    break
                else:
                    total_no_of_trees = (l + 1) * (l + 1)
                    trees_plotted = valid_tree_cells[bottom_row][bottom_col] - valid_tree_cells[bottom_row][top_col - 1] - \
                        valid_tree_cells[top_row - 1][bottom_col] + \
                        valid_tree_cells[top_row-1][top_col-1]
                    diff = total_no_of_trees - trees_plotted
                    if diff > k or result_square_size >= l + 1:
                        continue
                    elif (diff <= k and result_square_size < l + 1):
                        result_square_size = l + 1
                        result = [top_row, top_col, bottom_row, bottom_col]

    return result


valid_tree_cells = calculateMaxNoOfTrees(m, n, h, grid)
result = calculateMaxSquarePlot(m, n, h, k, valid_tree_cells, grid)
print(result[0], result[1], result[2], result[3])
