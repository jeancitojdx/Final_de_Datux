#MODULO 3 N° 3
#Informar el promedio de nota del curso total.

import val as v
aprobadas=0
desaprobadas=0
suma=0
sumapro=0
for i in range(0,v.alumnos):
    print("Ingrese nota del alumno "+str(i+1)+": ")
    
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        suma=suma +notas
        promedio=suma/3
    pass
print("la suma de notas es: ", suma)
print("promedio del curso es: ", suma/v.alumnos)
