print("#------Inicie Sesion------#")

pin_secreto=1234

pin=int(input("Ingrese pin: "))
while pin != pin_secreto:
    print("Intente de nuevo")
    pin=int(input("Ingrese pin: "))

print("Correcto!")
    