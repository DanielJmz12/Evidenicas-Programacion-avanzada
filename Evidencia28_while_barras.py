cantidad = 0
x = 1
n = int(input("numero de piezas analizar: "))

while n>=x:
    largo = float(input("ingresa la medida de la barra de acero: "))
    if largo>=2.3 and largo<=2.5:
        cantidad = cantidad+1
    x = x+1
print("cantidad piezas aptas para venta al publico: " + str(cantidad)) 
