def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock del producto: "))

    productos[nombre] = {"precio": precio, "cantidad": cantidad}
    print("Producto agregado correctamente.")


def procesar_compra(productos):
    carrito = {}
    continuar = "si"

    while continuar.lower() == "si":
        nombre = input("Ingrese el nombre del producto que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

        if nombre in productos:
            stock = productos[nombre]["cantidad"]

            if cantidad <= stock:
                if nombre in carrito:
                    carrito[nombre] += cantidad
                else:
                    carrito[nombre] = cantidad

                productos[nombre]["cantidad"] -= cantidad
                print("Producto agregado al carrito.")
            else:
                print("No hay suficiente stock del producto.")
        else:
            print("El producto no existe.")

        continuar = input("¿Desea agregar otro producto al carrito? (si/no): ")

    return carrito


def calcular_total(carrito, productos):
    total = 0

    for producto, cantidad in carrito.items():
        precio = productos[producto]["precio"]
        subtotal = precio * cantidad
        total += subtotal

    return total


def main():
    productos = {}

    while True:
        print("1. Agregar producto")
        print("2. Procesar compra")
        print("3. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_producto(productos)
        elif opcion == 2:
            carrito = procesar_compra(productos)
            total = calcular_total(carrito, productos)
            print("El total de la compra es:", total)
        elif opcion == 3:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    print("Gracias por utilizar la caja registradora.")


if __name__ == "__main__":
    main()