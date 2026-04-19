
tareas=["Revisar el codigo","corregir errores","mejorar diseño","agregar carrito"]
tareaslista=[]
contador=0
for tarea in tareas:
    print("Tareas: ", tarea)
    pregunta=input("Haz hecho la tarea?: ")
    if pregunta == "si":
        print("tarea completada!")
        tareaslista.append(tarea)
        
    else:
        print("Tarea incompleta")

print("tareas completadas: ", tareaslista)