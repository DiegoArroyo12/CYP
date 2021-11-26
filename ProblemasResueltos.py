# Problema 2.1

N = int(input("Introduce el número de de sonidos emitidos por un grillo en un minuto: "))

if N > 0: 
    T = N / 4 + 40
    print("Temperatura: ",T)
print("Fin del programa")

# Problema 2.2

P = int(input("Introduce un valor númerico entero a P: "))
Q = int(input("Introduce un valor númerico entero a Q: "))

EXP = P**3 + Q**4 - 2 * P**2

if EXP < 680:
    print(f"P:{P} Q:{Q}")
print("Fin del programa")

# Problema 2.3

A = float(input("Introduce un valor númerico entero a A: "))
B = float(input("Introduce un valor númerico entero a B: "))
C = float(input("Introduce un valor númerico entero a C: "))

DIS = (B**2) - (4*A*C)

if DIS > 0:
    X1 = (((-B)+DIS**0.5)/(2*A))
    X2 = (((-B)-DIS**0.5)/(2*A))
    print(f"Raíces Reales: X1={X1} X2={X2}")
print("Fin del programa")

# Problema 2.4

MAT = int(input("Introduce tu matrícula: "))
CAL1 = float(input("Introduce tu primera calificación: "))
CAL2 = float(input("Introduce tu segunda calificación: "))
CAL3 = float(input("Introduce tu tercera calificación: "))
CAL4 = float(input("Introduce tu cuarta calificación: "))
CAL5 = float(input("Introduce tu quinta calificación: "))

PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5

if PRO >= 6:
    print(f"Matrícula: {MAT} Promedio: {PRO} 'APROBADO' ")
else:
    print(f"Matrícula: {MAT} Promedio: {PRO} 'NO APROBADO' ")
print("Fin del programa")

# Problema 2.5 

NUM = int(input("Ingresa un número entero: "))

if NUM > 0:
    print(f"{NUM} es 'POSITIVO'")
else: 
    if NUM == 0: 
        print(f"{NUM} es 'NULO'")
    else:
        print(f"{NUM} es 'NEGATIVO'")
print("Fin del programa")

# Problema 2.6

A = int(input("Introduce un valor entero: "))

if A == 0: 
    print(f"{A} es 'NULO'")
else:
    if ((-1)**A) > 0:
        print(f"{A} es 'PAR'")
    else:
        print(f"{A} es 'IMPAR'")
print("Fin del programa")

# Problema 2.7 

A = int(input("Introduce un número entero: "))
B = int(input("Introduce otro número entero distinto: "))
C = int(input("Introduce un último número entero distinto a los anteriores: "))

if A < B:
    if B < C:
        print("Los números están en orden creciente")
    else: 
        print("Los números no están en orden creciente")
else:
    print("Los números no están en orden creciente")
print("Fin del programa")

# Problema 2.8 

COMPRA = float(input("Ingresa el monto de tu compra: "))

if COMPRA < 500:
    PAGAR = COMPRA
    print(f"Pagar: ${PAGAR}")
else: 
    if COMPRA <= 1000:
        PAGAR = COMPRA - (COMPRA * 0.05)
        print(f"Pagar: ${PAGAR}")
    else: 
        if COMPRA <= 7000:
            PAGAR = COMPRA - (COMPRA * 0.11)
            print(f"Pagar: ${PAGAR}")
        else: 
            if COMPRA <= 15000: 
                PAGAR = COMPRA - (COMPRA * 0.18)
                print(f"Pagar: ${PAGAR}")
            else: 
                PAGAR = COMPRA - (COMPRA * 0.25)
                print(f"Pagar: ${PAGAR}")
print("Fin del programa")

# Problema 2.9 

PREBAS = float(input("Ingrese el valor del producto: "))

if PREBAS > 500: 
    IMP = 20*0.30 + (PREBAS - 40)*0.50
    PRETOT = PREBAS + IMP
    print(f"Por la compra de ${PREBAS} Se debe pagar: {PRETOT}")
else:    
    if PREBAS > 40:
        IMP = 20*0.30 + (PREBAS - 40)*0.40
        PRETOT = PREBAS + IMP
        print(f"Por la compra de ${PREBAS} Se debe pagar: {PRETOT}")
    else:
        if PREBAS > 20:
            IMP = (PREBAS - 20)*0.30
            PRETOT = PREBAS + IMP
            print(f"Por la compra de ${PREBAS} Se debe pagar: {PRETOT}")
        else:
            IMP = 0 
            PRETOT = PREBAS + IMP
            print(f"Por la compra de ${PREBAS} Se debe pagar: {PRETOT}")
print("Fin del progama")

# Problema 2.10

A = int(input("Introduce un número: "))
B = int(input("Introduce otro número: "))
C = int(input("Introduce un último número: "))

if A > B:
    if A > C: 
        print(f"{A} es el número mayor")
    else:
        if A == C:
            print(f"{A} y {C} son los números mayores")
        else: 
            print(f"{C} es el número mayor")
else: 
    if A == B: 
        if A > C:
            print(f"{A} y {B} son los números mayores")
        else: 
            if A == C:
                print(f"{A} , {B} y {C} son iguales")
            else: 
                print(f"{C} es el número mayor")
    else: 
        if B > C: 
            print(f"{B} es el número mayor")
        else: 
            if B == C:
                print(f"{B} y {C} son los números mayores")
            else:
                print(f"{C} es el número mayor")
print("Fin del programa")

# Ejemplo 2.11

CLAVE = int(input("Introduzca su clave: "))
NUMIN = int(input("Introzca los minutos de su llamada: "))

if CLAVE == 12:
    COST = NUMIN*2
    print("Costo total de la llamada: $",COST)
elif CLAVE == 15:
    COST = NUMIN*2.2
    print("Costo total de la llamada: $",COST)
elif CLAVE == 18:
    COST = NUMIN*4.5
    print("Costo total de la llamada: $",COST)
elif CLAVE == 19:
    COST = NUMIN*3.5
    print("Costo total de la llamada: $",COST)
elif CLAVE == 23 or CLAVE == 25:
    COST = NUMIN*6
    print("Costo total de la llamada: $",COST)
else:
    COST = NUMIN*5
    print("Costo total de la llamada: $",COST)
print("Fin del programa")

# Problema 2.12

SUE = float(input("Ingrese su sueldo: "))
CATE = int(input("¿Cuál es su categoría?: "))
HE = int(input("Ingrese sus horas extra: "))

if CATE >= 1 and CATE <= 4:
    if CATE == 1:
        PHE = 30
    elif CATE == 2:
        PHE = 38
    elif CATE == 3:
        PHE = 50
    else:
        PHE = 70
else:
    PHE = 0

if HE > 30:
    NSUE = SUE + 30*PHE
else: 
    NSUE = SUE + HE*PHE
print("El nuevo sueldo es: $",NSUE)
print("Fin del programa")

# Problema 2.13

MAT = int(input("Ingrese su matrícula: "))
CARR = str(input("Ingrese la carrera que cursa: "))
SEM = int(input("Ingrese el semestre que cursa: "))
PROM = float(input("Ingrese su promedio: "))

if CARR == "Economía":
    if SEM >= 6 and PROM >= 8.8:
        print(f"Matrícula: {MAT} Carrera: {CARR} 'ACEPTADO'")
elif CARR == "Computación":
    if SEM > 6 and PROM > 8.5:
        print(f"Matrícula: {MAT} Carrera: {CARR} 'ACEPTADO'")
elif CARR == "Administración":
    if SEM > 5 and PROM > 8.5:
        print(f"Matrícula: {MAT} Carrera: {CARR} 'ACEPTADO'")
elif CARR == "Contabilidad":
    if SEM > 5 and PROM > 8.5:
        print(f"Matrícula: {MAT} Carrera: {CARR} 'ACEPTADO'") 
print("Fin del programa")