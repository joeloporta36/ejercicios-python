def calcular_promedio(nota1, nota2,nota3,nota4,nota5):
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    return promedio

n1=float(input("Ingrese nota 1: "))
n2=float(input("Ingrese nota 2: "))
n3=float(input("Ingrese nota 3: "))
n4=float(input("Ingrese nota 4: "))
n5=float(input("Ingrese nota 5: "))

resultado = calcular_promedio(n1,n2,n3,n4,n5)

print("El promedio es: ", resultado)