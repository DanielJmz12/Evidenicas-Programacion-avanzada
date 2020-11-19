preguntas = int(input("ingrese cuantas preguntas tenia el examen: "))
respuestas = int(input("ingrese cuantas respuestas correctas tiene el postulante: "))

division = respuestas/preguntas
promedio = division*100

if promedio>=90:
    print("nivel maximo")
elif promedio>=75:
    print("nivel medio")
elif promedio>=50:
    print("nivel regular")  
elif promedio<50:
    print("fuera de nivel")
