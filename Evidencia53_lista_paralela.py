nombres = []
edades = []

for x in range(5):
    nombre = input("ingresa el nombre: ")
    nombres.append(nombre)
    edad = int(input("ingresa la edad: "))
    edades.append(edad)

print("nombres de las personas mayores de edad: ")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
