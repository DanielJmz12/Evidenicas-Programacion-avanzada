dia = int(input("ingresa el dia: "))
mes = int(input("ingresa el mes: "))
año = int(input("ingresa el año: "))

if mes==1 or mes==2 or mes==3:
    print("corresponde al primer trimestre")
else:
    if mes==4 or mes==5 or mes==6:
        print("corresponde al segundo trimestre")
    else:
        if mes==7 or mes==8 or mes==9:
            print("corresponde al tercer trimestre")
        else:
            if mes==10 or mes==11 or mes==12:
                print("corresponde al cuarto trimestre")
        
