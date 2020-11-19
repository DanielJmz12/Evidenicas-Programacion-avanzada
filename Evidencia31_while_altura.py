personas = int(input("ingrese el numero de personas: "))
x = 1
n = 0

while x<=personas:
    altura = int(input("ingresa la altura: "))
    n = n+altura
    x = x+1
prom = n/personas
print("el promedio de altura es: " + str(prom))
