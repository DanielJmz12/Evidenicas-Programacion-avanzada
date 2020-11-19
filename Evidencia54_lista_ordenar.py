sueldos = []

for x in range(5):
    valor = int(input("ingresa el sueldo: "))
    sueldos.append(valor)


print("lista sin ordenar de los sueldos: ")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux

print("sueldos de la lista ordenados: ")
print(sueldos)
