from settings import Colors
from transpose_matrix import transpose_matrix

print(f"{Colors.YELLOW}====================================={Colors.END}")
print(f"{Colors.YELLOW}======= Welcome in Mathmatica ======={Colors.END}")
print(f"{Colors.YELLOW}====================================={Colors.END}")

print(f"{Colors.LIGHT_BLUE}What do You want to calculate?{Colors.END}")
print(f"{Colors.BLUE}1. Transpose Matrix{Colors.END}")
choice = input()

match(choice):
    case '1':
        matrix = [[1,2,3], [1,2,3], [1,2,3], [1,2,3]]
        print(matrix)
        print(transpose_matrix(matrix))
