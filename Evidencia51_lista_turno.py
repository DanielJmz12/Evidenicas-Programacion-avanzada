turnoM = []
turnoV = []

print("sueldo turno matutino")
for x in range(4):
    sueldoM = float(input("ingrese sueldo: "))
    turnoM.append(sueldoM)
print("sueldo turno vespertino")
for x in range(4):
    sueldoV = float(input("ingrese sueldo: "))
    turnoV.append(sueldoV)
print("sueldo de los trabajadores de la mañana: ")
print(turnoM)
print("sueldo de los trabajadores de la tarde: ")
print(turnoV)
