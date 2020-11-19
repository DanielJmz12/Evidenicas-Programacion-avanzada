alturas = []
suma=0
mayor = 0
menor = 0
for x in range(5):
    valor = float(input("ingresa una altura: "))
    alturas.append(valor)
    suma = suma+valor
promedio = suma/5
print("el promedio de alturas es: ")
print(promedio)
for x in range(5):
        if alturas[x]>promedio:
            mayor = mayor+1
        else:
            if alturas[x]<promedio:
                menor=menor+1
            
print("personas mas altas al promedio: ")
print(mayor)
print("personas mas bajas al promedio: ")
print(menor)
