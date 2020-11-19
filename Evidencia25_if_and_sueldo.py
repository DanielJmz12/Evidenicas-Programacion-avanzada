sueldo = int(input("ingresa el sueldo del operario: "))
antiguedad = int(input("ingresa los años de antiguedad: "))

if sueldo<500 and antiguedad>=10:
    mult = sueldo*.20
    aumento = mult+sueldo
    print("su nuevo sueldo es: " + str(aumento))
else:
    if sueldo<500 and antiguedad<10:
        mult = sueldo*.05
        aumento = mult+sueldo
        print("su nuevo sueldo es: " + str(aumento))
    else:
        if sueldo>=500:
            print("su sueldo es: " + str(sueldo))
