#Problemas Diversos

import val as v
Alum =[]
for i in range(0,v.alumnos):
    print(f"Ingrese datos del alumno {i+1} ")
    Datos={
        'Nombre': input('Nombre : '),
        'Nota 1': input('Nota 1 : '),
        'Nota 2': input('Nota 2 : '),
        'Nota 3': input('Nota 3 : ')
    }
    Alum.append(Datos)
print(Alum)
