lista = []

for x in range(5):
    valor = int(input("ingresa valor: "))
    lista.append(valor)

mayor = lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor = lista[x]
print("lista: ")
print(lista)

print("numero mayor de la lista: ")
print(mayor)
