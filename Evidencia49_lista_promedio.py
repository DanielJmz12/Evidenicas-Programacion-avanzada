sueldos = []
suma = 0
for x in range(5):
    valor = float(input("ingresa el sueldo: "))
    sueldos.append(valor)
    suma = suma+valor
print("los sueldos de los trabajadores son: ")
print(sueldos)
promedio = suma/5
print("el promedio de los sueldos es: ")
print(promedio)
