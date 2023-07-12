num_intentos = 3  # Número máximo de intentos para ingresar el valor de N
valor_n = None  # Variable para almacenar el valor de N

while num_intentos > 0:
    entrada_n = input("Introduce el valor de N (debe ser al menos 4 dígitos): ")
    if len(entrada_n) < 4:
        print("El número debe tener al menos 4 dígitos.")
        num_intentos -= 1
    else:
        try:
            valor_n = int(entrada_n)
            break
        except ValueError:
            print("Debes ingresar un número válido.")
            num_intentos -= 1

if valor_n is None:
    print("Has agotado el número máximo de intentos.")
else:
    cantidad_numeros = int(input("Introduce la cantidad de números aleatorios a generar: "))
    
    for i in range(cantidad_numeros):
        cuadrado = valor_n ** 2
        cuadrado_str = str(cuadrado)
        
        if len(cuadrado_str) < 4:
            print("Error al generar el número aleatorio. Inténtalo de nuevo.")
            break
        
        mitad = len(cuadrado_str) // 2
        digitos_centro = cuadrado_str[mitad-2:mitad+2]
        
        numero_aleatorio = float("0." + digitos_centro)
        
        # Mostrar resultados
        print(f"N{i+1} = {valor_n}")
        print(f"N{i+1}^2 = {cuadrado}")
        print(f"N{i+1}(aleatorio) = {numero_aleatorio}")
        print()
        
        valor_n = int(numero_aleatorio * 10000)