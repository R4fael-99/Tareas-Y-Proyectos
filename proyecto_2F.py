from matrix_m2 import matrix_multiply, gauss_jordan, cross_product, matrix_transpose, solve_linear_system, matrix_determinant

from encryption_m3 import generate_custom_key, encrypt, decrypt

from validation_m1 import valInt, valFloat, valComplex, valList

# Código 1: Encriptación

def main_encriptacion():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!? '
    # Generamos una clave personalizada
    custom_key = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA0987654321.!,? '

    key = generate_custom_key(alphabet, custom_key)
    
    print("\nBienvenido al programa de encriptación.")

    while True:
        print("\nSeleccione una opción:")
        print("1. Encriptar un mensaje")
        print("2. Desencriptar un mensaje")
        print("3. Salir")

        choice = input("Opción seleccionada:")

        if choice == '1':
            message = input("\nIngrese el mensaje que desea encriptar: ")
            encrypted_message = encrypt(message, key)
            print("Mensaje encriptado:", encrypted_message)
        elif choice == '2':
            encrypted_message = input("\nIngrese el mensaje encriptado: ")
            decrypted_message = decrypt(encrypted_message, key)
            print("Mensaje desencriptado:", decrypted_message)
        elif choice == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Código 2: Operaciones con matrices

# Función para ingresar una matriz desde el input
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Ingrese el elemento [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Función para ingresar un vector desde el input
def input_vector(length):
    vector = []
    for i in range(length):
        element = float(input(f"Ingrese el elemento [{i}]: "))
        vector.append(element)
    return vector

def main_matriz():
    print("\nBienvenido al Operador Matricial")
    while True:
    	
        print("\nOpciones:")
        print("1. Multiplicar matrices")
        print("2. Obtener la matriz inversa (Gauss-Jordan)")
        print("3. Calcular el producto vectorial")
        print("4. Transponer una matriz")
        print("5. Resolver un sistema de ecuaciones lineales")
        print("6. Calcular el determinante de una matriz")
        print("7. Salir")

        choice = int(input("Ingrese el número de la opción que desee: "))

        if choice == 1:
        # Solicitar al usuario el tamaño de las matrices
            rows1 = int(input("Ingrese el número de filas de la primera matriz: ")) 
            cols1 = int(input("Ingrese el número de columnas de la primera matriz: "))
            rows2 = int(input("Ingrese el número de filas de la segunda matriz: "))
            cols2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

        # Ingresar las matrices desde el input
            print("Ingrese los elementos de la primera matriz:")
            matrix1 = input_matrix(rows1, cols1)

            print("Ingrese los elementos de la segunda matriz:")
            matrix2 = input_matrix(rows2, cols2)

        # Realizar la multiplicación de matrices
            result_multiply = matrix_multiply(matrix1, matrix2)
            print("Resultado de la multiplicación de matrices:")
            print(result_multiply)
        # ... Código para la opción 1: Multiplicar matrices ...
        
        elif choice == 2:
        # Solicitar al usuario el tamaño de la matriz
            rows = int(input("Ingrese el número de filas de la matriz: "))
            cols = int(input("Ingrese el número de columnas de la matriz: "))

        # Ingresar la matriz desde el input
            print("Ingrese los elementos de la matriz:")
            matrix = input_matrix(rows, cols)

        # Obtener la matriz inversa (Gauss-Jordan)
            result_gauss_jordan = gauss_jordan(matrix)
            print("Matriz inversa (Gauss-Jordan):")
            print(result_gauss_jordan)
        # ... Código para la opción 2: Obtener la matriz inversa (Gauss-Jordan) ...
        
        elif choice == 3:
        # Ingresar los vectores desde el input
            print("Ingrese los elementos del primer vector:")
            vector1 = input_vector(3)

            print("Ingrese los elementos del segundo vector:")
            vector2 = input_vector(3)

        # Calcular el producto vectorial
            result_cross_product = cross_product(vector1, vector2)
            print("Producto vectorial:")
            print(result_cross_product)
        # ... Código para la opción 3: Calcular el producto vectorial ...
        
        elif choice == 4:
        # Solicitar al usuario el tamaño de la matriz
            rows = int(input("Ingrese el número de filas de la matriz: "))
            cols = int(input("Ingrese el número de columnas de la matriz: "))

        # Ingresar la matriz desde el input
            print("Ingrese los elementos de la matriz:")
            matrix = input_matrix(rows, cols)

        # Transponer la matriz
            result_transpose = matrix_transpose(matrix)
            print("Transpuesta de la matriz:")
            print(result_transpose)
        # ... Código para la opción 4: Transponer una matriz ...
        
        elif choice == 5:
        # Solicitar al usuario el tamaño de la matriz y el vector
            rows = int(input("Ingrese el número de filas de la matriz: "))
            cols = int(input("Ingrese el número de columnas de la matriz: "))

        # Ingresar la matriz desde el input
            print("Ingrese los elementos de la matriz:")
            matrix = input_matrix(rows, cols)

        # Ingresar el vector desde el input
            print("Ingrese los elementos del vector:")
            vector = input_vector(rows)

        # Resolver el sistema de ecuaciones lineales
            try:
                result_solve_system = solve_linear_system(matrix, vector)
                print("Resultado de la resolución del sistema de ecuaciones lineales:")
                print(result_solve_system)
            except ValueError as e:
                print("Error:", e)
        # ... Código para la opción 5: Resolver un sistema de ecuaciones lineales ...
        
        elif choice == 6:
        # Solicitar al usuario el tamaño de la matriz
            rows = int(input("Ingrese el número de filas de la matriz: "))
            cols = int(input("Ingrese el número de columnas de la matriz: "))

        # Ingresar la matriz desde el input
            print("Ingrese los elementos de la matriz:")
            matrix = input_matrix(rows, cols)

        # Calcular el determinante de la matriz
            result_determinant = matrix_determinant(matrix)
            print("Determinante de la matriz:")
            print(result_determinant)
        # ... Código para la opción 6: Calcular el determinante de una matriz ...
        elif choice == 7:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

#codigo 3: validacion

def main_validation():
    print("\nBienvenido al programa de validacion")
    while True:
        try:
            print("\nOpciones disponibles:")
            print("1. Validación de valor entero")
            print("2. Validación de valor flotante")
            print("3. Validación de valor complejo")
            print("4. Validación de lista")
            print( "5. Salir")
            
            option = input("Elige una opción (1/2/3/4): ")
            
            if option == "1":
                value_input = input("Ingresa un valor: ")
                try:
                    value = int(value_input)
                except ValueError:
                    print("False")
                    continue

                interval_option = input("¿Deseas agregar un intervalo? (si/no): ").lower()
                if interval_option == "si":
                    interval = eval(input("Ingresa el intervalo como una lista o una tupla (e.g., [3, 9] o (4, 10)): "))
                    result = valInt(value, interval)
                elif interval_option == "no":
                    result = valInt(value)
                else:
                    print("Opción no válida. Por favor, ingresa 'si' o 'no'.")
                    continue

                print(f"Resultado: {result}")


            elif option == "2":
                value_input = input("Ingresa un valor: ")
                try:
                    value = float(value_input)
                    if value.is_integer():
                        value = int(value)
                except ValueError:
                    print("False")
                    continue

                interval_option = input("¿Deseas agregar un intervalo? (si/no): ").lower()
                if interval_option == "si":
                    interval = eval(input("Ingresa el intervalo como una lista o una tupla (e.g., [4.4, 9.05] o (4, 10)): "))
                    result = valFloat(value, interval)
                elif interval_option == "no":
                    result = valFloat(value)
                else:
                    print("Opción no válida. Por favor, ingresa 'si' o 'no'.")
                    continue

                print(f"Resultado: {result}")

            elif option == "3":
                value_input = input("Ingresa un valor complejo (ejemplo: 3+4j): ")

                if "+" not in value_input or "j" not in value_input:
                    print("False")
                    continue

                try:
                    value = complex(value_input)
                except ValueError:
                    print("False")
                    continue

                interval_option = input("¿Deseas agregar un intervalo? (si/no): ").lower()
                if interval_option == "si":
                    interval = eval(input("Ingresa el intervalo como una lista o una tupla (e.g., [5, 10] o (4, 8)): "))
                    result = valComplex(value, interval)
                elif interval_option == "no":
                    result = valComplex(value)
                else:
                    print("Opción no válida. Por favor, ingresa 'si' o 'no'.")
                    continue

                print(f"Resultado: {result}")

            elif option == "4":
                arg1 = eval(input("Ingresa el primer argumento: "))
            
                if isinstance(arg1, list):
                    print(f"El primer argumento es True.")
                    
                    option = input("¿Qué opción del argumento 3 deseas ('len' o 'value')?: ").lower()
                    if option == 'len':
                        arg2 = input("Ingresa el segundo argumento (un número entero o una lista): ")
                        try:
                            arg2 = int(arg2)
                            arg3 = 'len'
                        except ValueError:
                            try:
                                arg2 = eval(arg2)
                                if not isinstance(arg2, list):
                                    raise TypeError("El segundo argumento no es válido para la opción 'len'.")
                                arg3 = 'len'
                            except:
                                raise ValueError("El segundo argumento no es válido para la opción 'len'.")
                    elif option == 'value':
                        arg2 = eval(input("Ingresa el segundo argumento (otra lista): "))
                        arg3 = 'value'
                    else:
                        raise ValueError("(valueError): El argumento 3 debe ser 'len' o 'value'.")
                        continue

                    result = valList(arg1, arg2, arg3)
                    print(f"Resultado: {result}")
                else:
                    print("False")
            elif option == "5":
                print("hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida (1/2/3/4).")
                continue
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")            

if __name__ == "__main__":
    print("¿Qué operación desea realizar?")
    print("1. Operación de encriptación")
    print("2. Operaciones con matrices")
    print("3. Operacion de validacion")

    operation_choice = int(input("Ingrese el número de la operación que desee realizar: "))

    if operation_choice == 1:
        main_encriptacion()
    elif operation_choice == 2:
        main_matriz()
    elif operation_choice == 3:
    	main_validation()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")