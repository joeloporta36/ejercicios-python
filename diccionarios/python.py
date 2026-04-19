producto =["Laptop","Mouse","Reloj"];

carrito=[]

Precio={
    "Laptop":200000,
    "Mouse":70000,
    "Reloj":50000
}
opcion=""
print("--Menu--")
while opcion != "4":
    print("\n 1 = Ver productos")
    print("2 = Agregar producto al carrito")
    print("3 = Ver carrito")
    print("4 = salir")
    opcion=input("Digite una oopción")

    if opcion == "1":
        print("__\n Productos disponibles__")
        for producto in producto:
            print(producto, "- $", Precio[producto])
    elif opcion == "2":
        print("__Agregar producto__")
        nombre=(input("ingrese nombre del producto: "))
        if nombre in producto:
            carrito.append(nombre)
            print("producto agregado al carrito")
        else:
            print("producto no existente")
    elif opcion == "3":
        print(carrito)
    

