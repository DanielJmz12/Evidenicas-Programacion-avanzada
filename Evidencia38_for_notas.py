aprobados = 0
reprobados = 0

for f in range (10):
    nota = int(input("ingresa la nota: "))
    if nota>=7:
        aprobados = aprobados+1
    else:
        reprobados = reprobados+1
print("alumnos aprobados: " + str(aprobados))
print("alumnos reprobados: " + str(reprobados))
