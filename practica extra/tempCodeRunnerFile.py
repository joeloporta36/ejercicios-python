estudiantes=int(input("¿Cuantos estudiantes hay?:"))
for i in range(estudiantes):
    suma=0
    
    for i in range(3):
        nota=int(input("Ingrese las notas:"))
        
        suma+= nota
        promedio = suma / 3

        if promedio >= 70:
            print("Aprobado 🔥")
        elif promedio < 69:
            print("reprobado")




