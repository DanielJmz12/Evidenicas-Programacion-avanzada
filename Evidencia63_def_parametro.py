def mostrar_mensaje(mensaje):
    print("______________________________________")
    print(mensaje)
    print("______________________________________")

def mostrar_suma():
    valor1 = int(input("ingresa el primer valor: "))
    valor2 = int(input("ingresa el segundo valor: "))
    suma = valor1+valor2
    print("la suma es: ",suma)

mostrar_mensaje("el programa muestra la suma de 2 numeros")
mostrar_suma()
mostrar_mensaje("hasta luego")
