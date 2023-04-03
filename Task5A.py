m, n, h = map(int, input().split())
grid = []

for i in range(0, m):
    row = list(map(int, input().split()))
    grid.append(row)

"""We calculate a binary matrix as follows -
    If the value of the plot is greater than or equal to h then mark the plot as 1 in binary matrix else mark it as zero.
    This matrix is required to compute the largest square of 1's with coner plots can be either 0 or 1.
"""


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


"""
opt matrix - we compute the opt matrix which stores the result the maximum square that can be formed.
once opt is computed we can get the maximum element which indcates the size of maximu  square and 
using this size and the plot where this size is achieved (i,j) we can find the indices of the max square that can be formed.

for each and every elemet in the binary matrix we check the diagonal, right and below plots and compute the size of
largest square that can be formed at that plot. Here, if the value of the plot is 2 , then this implies that we
can form a square of length 4. Similarly value 3 indicates a square of four and so on....... 

"""


def formulatePrecomputedMatrix(row, col, binary_matrix, opt, m, n):
    # base case
    if row == m or col == n or binary_matrix[row][col] == 0:
        return 0

    # check if the value exists in the table computed
    elif opt[row][col] != -1:
        return opt[row][col]

    # recursive case for checking the right , below and diagonal elements and iterating through the entire matrix
    right = formulatePrecomputedMatrix(row, col + 1, binary_matrix, opt, m, n)
    below = formulatePrecomputedMatrix(row + 1, col, binary_matrix, opt, m, n)
    diagonal = formulatePrecomputedMatrix(
        row + 1, col + 1, binary_matrix, opt, m, n)

    opt[row][col] = 1 + min(right, below, diagonal)

    return opt[row][col]


""""since the corner plots can be any value, the matrix of size 1 and 2 will have the largest possible matrix as the 
entire matrix because all the elements in this case are corners. Else condition handles the case of matrices 
of length greater than 2."""

if m == 1 and n == 1:
    print(0, 0, 0, 0)
elif m < 2 and n < 2:
    print(0, 0, 1, 1)
else:
    binary_matrix = calculateBinaryMatrix(m, n, h, grid)
    opt = [[-1]*(n) for i in range(m)]
    max_size = 0
    result_row = result_col = 0
    #this runs for at max O(mn) time
    for i in range(0, m):
        for j in range(0, n):
            if opt[i][j] == -1:
                opt[i][j] = formulatePrecomputedMatrix(
                    i, j, binary_matrix, opt, m-1, n-1)
                #calculate the maximum square size so far
                if (opt[i][j] > max_size):
                    result_row = i
                    result_col = j
                    max_size = opt[i][j]
    result = [result_row, result_col, result_row +
              max_size + 1, result_col + max_size + 1]

    print(result[0], result[1], result[2], result[3])
