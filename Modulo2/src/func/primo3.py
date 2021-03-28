
# importacion de librerias

# constantes

# funciones y metodos
def es_primo(numero):
    for n in range(2, numero, 1):
        print(f'el residuo de la division de {numero} / {n} es :{numero % n}')
        if numero % n ==0:
            return False
    return True

# #  mi programa principal
if __name__ == "__main__":
    print('ejecutando desde archivo primos3.py')
    # ingreso de numero por teclado
    numero = int(input('Ingrese un numero: '))
    # imprimo según validacion
    if es_primo(numero):
        print(f'el numero: {numero} es primo')
    else:
        print(f'el numero: {numero} NO es primo')