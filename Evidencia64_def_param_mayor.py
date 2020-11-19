def mostrar_mayor(v1,v2,v3):
    print("el valor mayor de los 3 es: ")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)

def cargar_valores():
    valor1 = int(input("ingresa primer valor: "))
    valor2 = int(input("ingresa segundo valor: "))
    valor3 = int(input("ingresa tercer valor: "))
    mostrar_mayor(valor1,valor2,valor3)

cargar_valores()
