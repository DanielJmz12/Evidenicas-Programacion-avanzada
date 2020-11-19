cal1 = int(input("ingresa primer calificacion: "))
cal2 = int(input("ingresa segunda calificacion: "))
cal3 = int(input("ingresa tercer calificacion: "))

suma = cal1+cal2+cal3
promedio = suma/3

if promedio>=7:
    print("aprobado")
else:
    if promedio>=4:
        print("regular")
    else:
        print("reprobado")
