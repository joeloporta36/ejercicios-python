contador=0


while contador < 5:
    nombre=str(input("Ingrese su nombre: "))
    edad=int(input("Ingrese su edad: "))

    if edad < 18:
        print("Lo sentimos ",nombre, "solo se permiten adultos")

    elif edad < 0 or edad > 120:
        print("Error: Edad no valida")
    elif edad >= 18:
        print(nombre, "registrado con éxito 🔥🔥")
        contador+=1
        
print("Registro completo. Lista de invitados cerrada, invitados:", contador )

    

    


