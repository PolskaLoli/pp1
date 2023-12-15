def identity_matrix(n):
     return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def display(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

# Wygeneruj trzy macierze jednostkowe o rozmiarach 3, 5 i 8
matrix_3 = identity_matrix(3)
matrix_5 = identity_matrix(5)
matrix_8 = identity_matrix(8)


print(matrix_3)