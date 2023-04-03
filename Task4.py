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
                binary_matrix[row][col] = 1
    return binary_matrix


"""
Compute a pre computed matrix or a preprocessed matrix in such a way that, if the valueof a plot is 1 in the binary matrix,
then check for the neighbours if the plot is able to form a plus of size 2. If the plot satifies this condition, then it means that
a square of size 3 x 3 is the maximum square at the plot in the matrix.
"""


def formulatePrecomputedMatrix(m, n, binary_matrix):
    precomputed_matrix = [[0]*(n) for i in range(m)]
    for row in range(0, m):
        for col in range(0, n):
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                precomputed_matrix[row][col] = 0
            elif (binary_matrix[row][col] == 1):
                if binary_matrix[row-1][col] == 1 and binary_matrix[row][col-1] == 1 and binary_matrix[row+1][col] == 1 and binary_matrix[row][col+1] == 1:
                    precomputed_matrix[row][col] = precomputed_matrix[row - 1][col] + 1
    return precomputed_matrix


""" Function that calculates the maximum size of the square with the value of each plot greater
than or equal to h

After computing the pre computed matrix, we use that matrix to find the largest square size. We traverse through every row 
in the precomputed matrix and for each and every element in the row, we find the sequenc of numbers that are 
greater than or equal to that number. Once we get this information, if the element is n and if there are n such elements or greater
in sequence then there is a square of size n + 2 that can be formed with this element.

Example - If a number n is 3 and it is repeated 3 times, then we have a square of size 5. similarly if n is 2 and it is repeated 2 then 
a square of size 4 can be formed with the given matrix. 
"""


def calculateMaxSquarePlot(m, n, precomputed_matrix):
    result = []
    result_square_size = 0
    col_end = 0
    row_end = 0
    for row in range(0, m):
        for col in range(0, n):
            count_of_element = 0
            for i in range(col, n):
                if precomputed_matrix[row][i] >= precomputed_matrix[row][col]:
                    count_of_element += 1
                else:
                    break

                if count_of_element >= precomputed_matrix[row][col] - 1:
                    if result_square_size <= precomputed_matrix[row][col] + 1:
                        result_square_size = precomputed_matrix[row][col] + 1
                        col_end = i + 2
                        row_end = row + 2
                    break
            count_of_element = 0
            for i in range(col, -1, -1):
                if precomputed_matrix[row][i] >= precomputed_matrix[row][col]:
                    count_of_element += 1
                else:
                    break
                if count_of_element >= precomputed_matrix[row][col] - 1:
                    if result_square_size <= precomputed_matrix[row][col] + 1:
                        result_square_size = precomputed_matrix[row][col] + 1
                        col_end = col + 2
                        row_end = row + 2
                    break

    result = [row_end - result_square_size, col_end -
              result_square_size, row_end, col_end]

    return result


""""since the corner plots can be any value, the matrix of size 1 and 2 will have the largest possible matrix as the 
entire matrix because all the elements in this case are corners. Else condition handles the case of matrices 
of length greater than 2."""

if m == 1 and n == 1:
    print(0, 0, 0, 0)
elif m < 2 and n < 2:
    print(0, 0, 1, 1)
else:
    binary_matrix = calculateBinaryMatrix(m, n, h, grid)
    precomputed_matrix = formulatePrecomputedMatrix(m, n, binary_matrix)
    result = calculateMaxSquarePlot(m, n, precomputed_matrix)
    print(result[0], result[1], result[2], result[3])
