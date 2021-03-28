while True:
    try:
        alumnos=int(input("Ingrese cantidad de alumnos:"))
        break
    except ValueError:
        print("Error, Ingrese un dato correcto ")