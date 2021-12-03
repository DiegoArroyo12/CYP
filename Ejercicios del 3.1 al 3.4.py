# Problema 3.1

SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
I = 1
while I <= 270:
    NUM = int(input("Ingresa un número entero: "))
    if NUM != 0: 
        if ((-1)**NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
        else:
            SUMIMP += NUM
    I += 1
PROPAR = SUMPAR/CUEPAR
print(PROPAR," ", SUMIMP)

# Problema 3.2 

SUMSER = 0
BAND = "T"
I = 2
while I <= 1800:
    SUMSER += 1
    print(I)
    if BAND == "T":
        BAND = "F"
        I += 3
    else: 
        BAND ="T"
        I += 2
print(f"Hay {SUMSER} números en esta serie")

# Problema 3.3

SERIE = 0
N = int(input("Ingresa un número: "))
BAND = "T"
I = 1
while I <= N:
    if BAND == "T":
        SERIE = (SERIE + 1)/I
        BAND = "F"
    else: 
        SERIE = (SERIE - 1)/I
        BAND = "T"
    I += 1
print(SERIE)

# Problema 3.4

NOM = 0 
SUE = float(input("Ingrese su sueldo: "))
while SUE != -1:
    if SUE < 1000:
        NSUE = SUE*1.15
    else:
        NSUE = SUE*1.12
    NOM += NSUE
    print("El nuevo sueldo es: ",NSUE)
    SUE = float(input("Ingrese su sueldo: "))
print("La nómina es: ",NOM)