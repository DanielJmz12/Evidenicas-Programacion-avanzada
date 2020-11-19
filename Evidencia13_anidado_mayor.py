num1 = int(input("ingresa el primer valor: "))
num2 = int(input("ingresa el segundo valor: "))
num3 = int(input("ingresa el tercer valor: "))

if num1>num2:
    if num1>3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
