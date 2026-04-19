Productos=("Laptop","Mouse","Reloj");

carrito={}

Precio={
    "Laptop":200.000,
    "Mouse":70.000,
    "Reloj":50.000
}
print("--Menu--")
while opcion != 4:
    print("\n 1 = Ver productos")
    print("2 = AgregarProducto")
    print("3 = Ver carrito")
    print("4 = salir")
    opcion=input("Digite una oopción")

    if opcion == "1":
        print(Productos)
    elif opcion == "2":
        nombre=input("Ingrese el nombre del producto")
        carrito[nombre]=""
    elif opcion == "3":
        print(carrito)

print("Productos:", carrito)