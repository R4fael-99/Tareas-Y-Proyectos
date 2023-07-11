productos = {}

while True:
    print("1. Agregar producto")
    print("2. Procesar compra")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock del producto: "))

        if nombre in productos:
            print("El producto ya existe. Actualizando información...")
            productos[nombre]["precio"] = precio
            productos[nombre]["cantidad"] = cantidad
        else:
            productos[nombre] = {"precio": precio, "cantidad": cantidad}

        print("Producto agregado correctamente.")
    elif opcion == 2:
        if not productos:
            print("No hay productos en el inventario.")
            continue

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

        total = sum(productos[producto]["precio"] * cantidad for producto, cantidad in carrito.items())

        print("Resumen de compra:")
        for producto, cantidad in carrito.items():
            precio = productos[producto]["precio"]
            subtotal = precio * cantidad
            print(f"{producto}: {cantidad} x {precio} = {subtotal}")

        print("El total de la compra es:", total)
    elif opcion == 3:
        if not productos:
            print("No hay productos en el inventario.")
            continue

        print("Inventario:")
        for nombre, detalles in productos.items():
            precio = detalles["precio"]
            cantidad = detalles["cantidad"]
            print(f"{nombre} - Precio: {precio}, Cantidad en stock: {cantidad}")
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print("Gracias por utilizar la caja registradora.")