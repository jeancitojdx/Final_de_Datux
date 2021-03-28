#MODULO 1
#EJERCICIO 1

nombre = input("¿Cual es su nombre? ")
print('Hello {}'.format(nombre))

#EJERCICO 2

import string

print(string.ascii_lowercase)

a = input("Ingrese el abecedario alterado que desea: ")

s = input("Ingrese oracion que quiere encriptar con el abecedario anteriormente proporcionado: ")

a = a.lower()

s=s.lower()

acumulador=[]

for i in s:    
    for j in string.ascii_lowercase:
        indice = string.ascii_lowercase.index(j)
        if i == j:


            for k in a:
                indice1 = a.index(k)
                if j == k:
                    acumulador.append(indice1) 




acumuladora=[]
for i in acumulador:    
    acumuladora = acumuladora + [i]    

g = ""  

for i in acumuladora:
    g = g + string.ascii_lowercase[i]
print (g)

#PROBLEMAS DIVERSOS 
#1
inversion= float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))

#2
from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática "))
B = int(input("Ingrese el coeficiente de la variable lineal"))
C = int(input("Ingrese el término independiente"))
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A) 
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)