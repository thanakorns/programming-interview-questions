import numpy as np

def setZeros(matrix):
    col_list = []
    row_list = []
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] == 0 and col_list.index(j) < 0 and row_list.index(i) < 0:
                col_list.append(j)
                row_list.append(i)
    for col in col_list:
        matrix[:][col] = 0
    for row in row_list:
        matrix[row] = 0
    return matrix


def setZerosEfficient(matrix):
    firstRowHasZero = False
    firstColHasZero = False
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            firstRowHasZero = True
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColHasZero = True

    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            nullify(matrix, -1, i)

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullify(matrix, i, -1)

    if firstColHasZero:
        nullify(matrix, -1, 0)

    if firstRowHasZero:
        nullify(matrix, 0, -1)


def nullify(matrix, row, col):
    #nullify ith row
    if row >= 0 and col < 0:
        for i in range(len(matrix)):
            matrix[i] = 0

    #nullify ith column
    if col >= 0 and row < 0:
        for i in range(len(matrix[0])):
            matrix[:][i]= 0

matrix = np.array([[2,2],[2,2]])
matrix[:,1] = 0
print(matrix)


