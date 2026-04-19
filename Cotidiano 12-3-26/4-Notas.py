print(("---Validador de Notas---"))
nota=int(input("Ingrese su nota: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70 and 89:
    print("Aprobado")
elif nota < 70:
    print("Reprobado")
else:
    print("nota no valida")
