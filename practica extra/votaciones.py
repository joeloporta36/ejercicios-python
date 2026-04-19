Laura=0
Ariel=0
Fabricio=0

personas=int(input("¿Cuantas personas van a votar?"))
for i in range(personas):
    voto=int(input("Ingrese su voto:"))
    if voto == 1:
        print("Haz votado por Laura 😎")
        Laura+=1
    elif voto == 2:
        print("Haz votador por Ariel 😕")
        Ariel+=1
    elif voto == 3:
        print("Haz votador por Fabricio ")
        Fabricio+=1

print("------ RESULTADOS -----")
print("Laura:", Laura)
print("Ariel:", Ariel)
print("Fabricio:", Fabricio)

if Laura > Ariel and Laura > Fabricio:
    print("Laura como presidente 🔥🎈")
elif Ariel > Laura and Ariel > Fabricio:
    print("Ariel como  presidente 🐈")
elif Fabricio > Laura and Fabricio > Ariel:
    print("Fabricio como presidente!")
    
