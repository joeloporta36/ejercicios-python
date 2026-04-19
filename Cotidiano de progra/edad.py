for i in range(4):
    edad=int(input("Ingrese su edad:"))


    while edad < 0:
        print("edad no valida")
        edad=int(input("Ingrese su edad:"))

    if edad >= 18:
        print("puede ingresar")
    else:
        print("no puede ingresar")
   