def matrix_multiply(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def gauss_jordan(matrix):
    n = len(matrix)
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for col in range(n):
        pivot_row = max(range(col, n), key=lambda i: abs(augmented_matrix[i][col]))
        augmented_matrix[col], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[col]

        pivot_val = augmented_matrix[col][col]
        if pivot_val == 0:
            raise ValueError("La matriz no se puede invertir.")

        for j in range(col, 2 * n):
            augmented_matrix[col][j] /= pivot_val

        for i in range(n):
            if i == col:
                continue
            factor = augmented_matrix[i][col]
            for j in range(col, 2 * n):
                augmented_matrix[i][j] -= factor * augmented_matrix[col][j]

    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix

def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Los vectores deben tener longitud 3 para calcular el producto vectorial.")

    result = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]
    return result

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def solve_linear_system(coeff_matrix, const_vector):
    n = len(coeff_matrix)

    # Transformar la matriz aumentada [coeff_matrix | const_vector]
    augmented_matrix = [coeff_matrix[i] + [const_vector[i]] for i in range(n)]

    # Eliminación gaussiana
    for col in range(n):
        if augmented_matrix[col][col] == 0:
            raise ValueError("El sistema no tiene solución única.")

        for row in range(col + 1, n):
            factor = augmented_matrix[row][col] / augmented_matrix[col][col]
            for j in range(col, n + 1):
                augmented_matrix[row][j] -= factor * augmented_matrix[col][j]

    # Sustitución hacia atrás para encontrar las soluciones
    solutions = [0] * n
    for i in range(n - 1, -1, -1):
        if augmented_matrix[i][i] == 0:
            raise ValueError("El sistema no tiene solución única.")

        solutions[i] = augmented_matrix[i][n] / augmented_matrix[i][i]
        for j in range(i):
            augmented_matrix[j][n] -= augmented_matrix[j][i] * solutions[i]

    return solutions

def matrix_determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    determinant = 0
    for i in range(n):
        submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        sign = (-1) ** i
        determinant += sign * matrix[0][i] * matrix_determinant(submatrix)

    return determinant
    
    