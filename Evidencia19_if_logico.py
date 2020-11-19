num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
num3 = int(input("ingresa el tercer numero: "))

print("el numero mayor es: ")

if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

