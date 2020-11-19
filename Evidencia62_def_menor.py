def menor_valor():
    valor1 = int(input("ingrese primer valor: "))
    valor2 = int(input("ingrese segundo valor: "))
    valor3 = int(input("ingresa tercer valor: "))
    print("menor de los tres")
    if valor1<valor2 and valor1<3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)

menor_valor()
menor_valor()
