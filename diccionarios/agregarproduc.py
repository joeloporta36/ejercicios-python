Producto={};

while True:
    nombre=input("Ingrese el nombre del Producto: ")
    precio= int(input("Ingrese precio: "));
    Producto[nombre] = precio
    continuar = input("Quieres agregar mas productos? (si/no): ")
    if continuar.lower() != "si":
        break
print(Producto)


