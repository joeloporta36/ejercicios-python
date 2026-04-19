#lista de frutas#
print("##LISTA DE FRUTAS##")

listafrutas=["manzana"," fresa", "piña", "sandia", "naranjas", "arandanos", "uvas", "melocoton", "banano", "guayaba"]
print(listafrutas)
#se agregan 2 elementos#
print("##SE AGREGAN 2 ELEMENTOS##")

listafrutas.append("aguacate")
listafrutas.append("pera")
print(listafrutas)
#modificar#
print("##MODIFICAR INDICE 2, 6 Y 9##")

listafrutas[1]="marandina"
listafrutas[5]="coco"
listafrutas[8]="aguacate"
print(listafrutas)
#mostrar#
print("##acceder al índice 3 y 7 mostrarlo ##")

print(listafrutas[3])
print(listafrutas[7])

#eliminar#
print("##eliminar 4 elementos de la lista##")

listafrutas.remove("aguacate")
listafrutas.remove("manzana")
listafrutas.remove("melocoton")
listafrutas.remove("pera")
print(listafrutas)

