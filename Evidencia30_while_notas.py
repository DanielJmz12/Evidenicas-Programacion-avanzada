x = 1
n = 0
n1 = 0

while x<=10:
    cal = int(input("ingresa la calificacion: "))
    if cal>=7:
        n = n+1
    else:
        n1 = n1+1
    x = x+1
print("numero de alumnos aprobados: " + str(n))
print("numero de alumnos reprobados: " + str (n1))


