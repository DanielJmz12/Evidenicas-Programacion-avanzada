lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(lista)
print("_______________________")

#imprimir el primer componente
print(lista[0])
print("_______________________")

#imprimir el primer componente de la lista
print(lista[0][0])
print("_______________________")

#imprimir lista de mi primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("_______________________")

#imprimir todos los componentes de la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
