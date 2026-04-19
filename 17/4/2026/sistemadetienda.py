Productos = {
    "Tablet": 250000,
    "Computadora": 300000,
    "Teclado": 67000,
    "Router": 85000,
    "Mouse": 50000
}

carrito = []

opcion = ""

while opcion != "6":
    print("\n--- SISTEMA DE TIENDA ---")
    print("1. Agregar productos con precio")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Comprar productos")
    print("5. Mostrar total a pagar")
    print("6. Salir")

    opcion = input("Escoja una opción: ")

    if opcion == "1":
        print("\n--- Agregar producto ---")
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        Productos[nombre] = precio
        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("\n--- Productos disponibles ---")
        for producto, precio in Productos.items():
            print(producto, ":", precio)

    elif opcion == "3":
        print("\n--- Buscar producto ---")
        buscar = input("Ingrese el nombre del producto: ")

        if buscar in Productos:
            print("Producto encontrado.")
            print("Precio:", Productos[buscar])
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("\n--- Comprar producto ---")
        for producto, precio in Productos.items():
            print(producto, ":", precio)

        comprar = input("¿Qué producto quiere comprar?: ")

        if comprar in Productos:
            carrito.append((comprar, Productos[comprar]))
            print("Producto agregado al carrito.")
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        print("\n--- Carrito de compras ---")
        total = 0

        if len(carrito) == 0:
            print("El carrito está vacío.")
        else:
            for producto, precio in carrito:
                print(producto, ":", precio)
                total += precio

            print("Total a pagar:", total)

    elif opcion == "6":
        print("Saliendo del programa...")

    else:
        print("Opción inválida.")