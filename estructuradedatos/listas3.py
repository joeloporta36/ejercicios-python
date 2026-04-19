#listas sin limites
frutas=[]

while True:
    dato=input("Digite un número (o escriba 'salir'): ")

    if dato == "salir":
        break

    frutas.append(dato)

print("frutas totales: ", frutas)