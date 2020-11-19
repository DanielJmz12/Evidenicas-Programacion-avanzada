def mostrar_resultado(a,p):
    resultado = input("¿quiere calcular el area y el perimetro del cuadrado? ")
    if resultado == "si":
        print("el area del cuadrado es: ",a)
        print("el perimetro del cuadrado es: ",p)
    else:
        if resultado == "no":
            print("el programa termino")

def cargar_valores():
    lado = int(input("ingresa el lado de un cuadrado: "))
    area = lado*lado
    perimetro = lado+lado+lado+lado
    mostrar_resultado(area,perimetro)

cargar_valores()


    
