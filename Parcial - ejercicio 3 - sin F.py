# Solicitar al usuario los valores de N y M
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

matriz = []
numero = 1
direccion = 1  # 1 para ir hacia la derecha, -1 para ir hacia la izquierda

for fila in range(N):
    if direccion == 1:
        matriz.append([numero + columna for columna in range(M)])
        direccion = -1
    else:
        matriz.append([numero + M - 1 - columna for columna in range(M)])
        direccion = 1

    numero += M

# Mostrar la matriz de zig-zag
for fila in matriz:
    print(fila)