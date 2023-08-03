# Pedir al usuario que ingrese un número válido
intentos_n1 = 0
while True:
    if intentos_n1 == 3:
        print("Límite de intentos alcanzado. Adiós.")
        break

    N1 = input("Por favor, ingresa un número: ")

    try:
        N1 = int(N1)
        N1_cuadrado = N1 ** 2
        cuadrado_str = str(N1_cuadrado)

        if len(cuadrado_str) >= 4:
            medio_N1_cuadrado = len(cuadrado_str) // 2
            N3 = cuadrado_str[medio_N1_cuadrado - 2:medio_N1_cuadrado + 2]
            print("N1^2 =", N1_cuadrado)
            print(f"N1 Aleatorio = 0.{N1_cuadrado}")
            print(f"N2 = {N3}")
            # Repetir el proceso con N3 hasta 3 veces
            for i in range(2,4):
                N3_cuadrado = int(N3) ** 2
                cuadrado_str_N3 = str(N3_cuadrado)
                medio_N3 = len(cuadrado_str_N3) // 2
                N3 = cuadrado_str_N3[medio_N3 - 2:medio_N3 + 2]
                print(f"N{i}^2 = ", N3_cuadrado)
                print(f"N{i} Aleatorio = 0.{N3_cuadrado}")
                print(f"N{i+1} =", N3)

            break
        else:
            print("El resultado no tiene al menos 4 dígitos. Intenta nuevamente.")
            intentos_n1 += 1
    except ValueError:
        print("Error: Ingresa un número válido.")
        intentos_n1 += 1
        