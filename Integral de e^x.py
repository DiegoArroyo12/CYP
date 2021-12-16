import math

def preg():
    print("\n¿Qué desea hacer?")
    print("1.- Introducir otro número")
    print("2.- Salir")


e = math.e
opcion = 1
while opcion == 1:
    N = int(input("Introduce el número de rectángulos que quieres: "))

    inx = (1/N)
    A = inx/2
    cont = 0 
    f1 = inx * (e**A)

    for x in range(1,N):
        i = A + inx
        A = i
        f2 = inx * (e**A)
        f1 += f2
    resultado = round((f1 + cont),5)
    print(f"El resultado de la integral con {N} rectángulos es de: {resultado}")
    preg()
    opcion = int(input("Su selección es: "))
    print(f"----- Su selección fue {opcion} -----")

    if opcion == 2: 
        print("FIN DEL PROGRAMA, HASTA LUEGO")