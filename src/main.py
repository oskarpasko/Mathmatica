from settings import Colors

print(f"{Colors.YELLOW}====================================={Colors.END}")
print(f"{Colors.YELLOW}======= Welcome in Mathmatica ======={Colors.END}")
print(f"{Colors.YELLOW}====================================={Colors.END}")

def cos(trans):
    trans = [ [0]*rows for i in range(columns)]

    print(trans)

    for row in range(rows):
        for col in range(columns):
            trans[col][row] = matrix[row][col]

    return trans

matrix = [[1,2,3], [1,2,3], [1,2,3], [1,2,3]]

rows = len(matrix)
columns = len(matrix[0])

print(matrix)

print(cos(matrix))
