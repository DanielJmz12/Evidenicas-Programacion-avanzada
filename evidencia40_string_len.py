#Funcion len
"""nombre=input("Ingrese su nombre : ")

print("Primer caracter : ")
print(nombre[0])

print("Cantidad total de letras del nombre : ")
print(len(nombre))"""

#vocales
"""nombre=input("Ingresa tu nombre : ")
if nombre[0]== "a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print("El nombre ingresado comienza con una vocal")
else:
    print("El nombre NO comienza con una vocal")"""

#@mail
"""mail=input("Ingresa un mail : ")
cantidad=0
x=0

while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1

if cantidad==1:
    print("Contiene solo un @ el mail")
else:
    print("Incorrecto")"""

#Funciones mayusculas y minusculas
nombre1="mAriA"
print(nombre1)

nombre2=nombre1.upper()
print(nombre2)

nombre3=nombre1.lower()
print(nombre3)

nombre4=nombre1.capitalize()
print(nombre4)

