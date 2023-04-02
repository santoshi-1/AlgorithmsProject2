from collections import deque

m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h"""


def calculateBinaryMatrix(m, n, h, grid):
    binaryMatrix = [[0]*(n) for i in range(m)]
    for row in range(0, m):
        for col in range(0, n):
            if grid[row][col] >= h:
                binaryMatrix[row][col] = 1
    return binaryMatrix


def formulatePrecomputedMatrix(m, n, binaryMatrix):
    preComputedMatrix = [[1]*(n) for i in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                preComputedMatrix[i][j] = 1
            else:
                if binaryMatrix[i-1][j] == 1 and binaryMatrix[i+1][j] == 1 and binaryMatrix[i][j-1] == 1 and binaryMatrix[i][j+1] == 1:
                    preComputedMatrix[i][j] = preComputedMatrix[i-1][j] + 1
    return preComputedMatrix


def calculateMaxSquarePlot(m, n, grid):
    result = []
    result_square_size = 0
    for row in range(0, m):
        stack = []
        arr = [0]*n
        for col in range(n-1, -1, -1):
            if len(stack) == 0:
                arr[col] = 1
                currElem = grid[row][col]
                stack.append(grid[row][col])
            else:
                if grid[row][col] == stack[len(stack)-1]:
                    arr[col] = 1 + arr[col + 1]
                    stack.append(grid[row][col])
                else:
                    if arr[col + 1] >= currElem - 1 and result_square_size < currElem + 1:
                        result_square_size = currElem + 1
                        index = col + arr[col + 1]
                        bottom_row = row + 2
                        bottom_col = index + 2
                        top_row = bottom_row - (currElem + 1) + 1
                        top_col = bottom_col - (currElem + 1) + 1
                        result = [top_row, top_col, bottom_row, bottom_col]

                    if grid[row][col] < stack[len(stack)-1]:
                        arr[col] = arr[col + 1] + 1
                    else:
                        stack = []
                        arr[col] = 1

                    currElem = grid[row][col]
                    stack.append(grid[row][col])

    return result


binaryMatrix = calculateBinaryMatrix(m, n, h, grid)
preComputedMatrix = formulatePrecomputedMatrix(m, n, binaryMatrix)
result = calculateMaxSquarePlot(m, n, preComputedMatrix)
print(result)
