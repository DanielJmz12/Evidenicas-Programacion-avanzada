num1 = int(input("ingresa el primer valor: "))
num2 = int(input("ingresa el segundo valor: "))
num3 = int(input("ingresa el tercer valor: "))

suma = num1+num2
mult = suma*num3
if num1==num2 and num1==num3:
    print(mult)
else:
    print("no se puede realizar la operacion")
