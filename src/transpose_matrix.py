def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = [ [0]*rows for i in range(columns)]

    for row in range(rows):
        for col in range(columns):
            transposed[col][row] = matrix[row][col]

    return transposed