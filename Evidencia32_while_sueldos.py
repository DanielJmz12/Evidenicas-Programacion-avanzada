empleados = int(input("ingresa el numero de empleados: "))
x=1
Min = 0
Max = 0
importe = 0

while x<=empleados:
    sueldo = int(input("ingresa el sueldo: "))
    importe = importe + sueldo
    if sueldo>=100 and sueldo<=300:
        Min = Min+1
    else:
        if sueldo>300:
            Max = Max+1
    x = x+1
print("numero de trabajadores que ganan entre 100 y 300 pesos: " + str(Min))
print("numero de trabajadores que ganan mas de 300 pesos: " + str(Max))
print("el importe de todos los trabajadores es: " + str(importe))
