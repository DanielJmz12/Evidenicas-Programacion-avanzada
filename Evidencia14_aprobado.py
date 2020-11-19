cal1 = int(input("ingresa primer calificaion: "))
cal2 = int(input("ingresa segunda calificaion: "))
cal3 = int(input("ingresa tercer calificaion: "))

suma = cal1+cal2+cal3
promedio = suma/3

if promedio>=7:
    print("promocionado")
else:
    print(" no promocionado")
