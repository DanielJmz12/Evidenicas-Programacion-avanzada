valor = int(input("ingresa un valor del 1 al 999: "))

if valor<9:
    print("el valor es de un digito")
elif valor<99:
    print("el valor es de dos digitos")
elif valor<999:
    print("el valor es de tres digitos")
elif valor>999:
    print("error excediste el numero permitido")
