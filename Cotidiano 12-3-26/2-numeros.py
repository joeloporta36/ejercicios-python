numero=(int(input("Ingrese un número entero:")))

if numero > 0:
    print("El número es positivo")
elif numero<0:
    print("El número es negativo")
else:
    print("El número es cero")


if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")