def generar_numero_aleatorio(semilla):
    # Elevar la semilla al cuadrado
    cuadrado = semilla ** 2
    
    # Convertir el cuadrado en una cadena
    cuadrado_str = str(cuadrado)
    
    # Verificar que la semilla tenga al menos 4 dígitos
    if len(cuadrado_str) < 4:
        print("El número inicial debe tener al menos 4 dígitos.")
        return None
    
    # Obtener los dígitos del centro
    mitad = len(cuadrado_str) // 2
    digitos_centro = cuadrado_str[mitad-2 : mitad+2]
    
    # Convertir los dígitos del centro en un número decimal
    numero_aleatorio = float("0." + digitos_centro)
    
    return numero_aleatorio

def solicitar_numero():
    num_intentos = 3
    while num_intentos > 0:
        n = input("Introduce el valor de N (debe ser al menos 4 dígitos): ")
        if len(n) < 4:
            print("El número debe tener al menos 4 dígitos.")
            num_intentos -= 1
        else:
            try:
                n = int(n)
                return n
            except ValueError:
                print("Debes ingresar un número válido.")
                num_intentos -= 1
    
    print("Has agotado el número máximo de intentos.")
    return None

def main():
    semilla = solicitar_numero()
    if semilla is None:
        return
    
    n = int(input("Introduce el número de elementos en la lista: "))
    
    numeros_aleatorios = []
    for i in range(n):
        numero_aleatorio = generar_numero_aleatorio(semilla)
        if numero_aleatorio is not None:
            numeros_aleatorios.append(numero_aleatorio)
            print(f"N{i+1} = {semilla}")
            print(f"N{i+1}^2 = {semilla**2}")
            print(f"N{i+1}(aleatorio) = {numero_aleatorio}")
            print()
            semilla = int(numero_aleatorio * 10000)  # Convertir la parte decimal en una nueva semilla

if __name__ == '__main__':
    main()