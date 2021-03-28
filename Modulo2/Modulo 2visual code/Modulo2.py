#Modulo 2
#Ejercicio 1

def numero(piramide):
    try:
        int(piramide)
        return True
    except ValueError:
        return False


n = input('Escriba un número entero: ')

while numero(n) is False:
    n = input('El numero que ingreso no es un numero: ')

n = int(n)    
    
while n < 0 or n > 8:
    n = int(input("Ingrese un valor entre 1 y 8: "))

for i in range (n+1):
    print(" "*(n-i)+"#"*i)

#cifrado de cesar
#parte 1

from string import ascii_lowercase, ascii_uppercase

def cifrado_cesar(texto, pasos):
    resultado = []

    for c in texto:
        if c in ascii_lowercase:
            indice = ascii_lowercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_lowercase)
            resultado.append(ascii_lowercase[nuevo_indice])
        elif c in ascii_uppercase:
            indice = ascii_uppercase.index(c)
            nuevo_indice = (indice + pasos) % len(ascii_uppercase)
            resultado.append(ascii_uppercase[nuevo_indice])
        else:
            resultado.append(c)

    return ''.join(resultado)

texto = 'Hello'
print(cifrado_cesar(texto, 1))




