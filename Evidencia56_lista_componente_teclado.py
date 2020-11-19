nombres = []
notas = []

for x in range(3):
    nom = input("ingresa el nombre del almuno: ")
    nombres.append(nom)

    no1 = int(input("ingresa la primer nota: "))
    no2 = int(input("ingresa la segunda nota: "))
    notas.append([no1,no2])

for x in range(3):
    print(nombres[x], notas[x][0], notas[x][1])
          
