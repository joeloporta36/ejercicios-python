estudiantes=int(input("¿Cuantos estudiantes hay?:"))
for i in range(estudiantes):
    suma=0
    
    for j in range(3):
        nota=int(input("Ingrese las notas:"))
        
        suma+= nota
       

        if promedio >= 70:
            print("Aprobado 🔥")
        elif promedio < 70:
            print("reprobado")
    promedio = suma / 3




