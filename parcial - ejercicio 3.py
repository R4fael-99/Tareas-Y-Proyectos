def generar_matriz_zigzag(n, m):
    matriz = [[0] * m for _ in range(n)]
    numero = 1
    direccion = 1  # 1 para ir hacia la derecha, -1 para ir hacia la izquierda

    for fila in range(n):
        if direccion == 1:
            for columna in range(m):
                matriz[fila][columna] = numero
                numero += 1
            direccion = -1
        else:
            for columna in range(m - 1, -1, -1):
                matriz[fila][columna] = numero
                numero += 1
            direccion = 1

    return matriz

# Solicitar al usuario los valores de N y M
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

# Generar y mostrar la matriz de zig-zag
matriz_zigzag = generar_matriz_zigzag(N, M)
for fila in matriz_zigzag:
    print(fila)