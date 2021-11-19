num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))
num3 = int(input("De nuevo dame número entero: "))
num4 = int(input("Dame un último número entero: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} es el número mayor")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} es el número mayor")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} es el número mayor")
else:
    print(f"{num4} es el número mayor")

if num1 < num2 and num1 < num3 and num1 < num4:
    print(f"{num1} es el número menor")
elif num2 < num1 and num2 < num3 and num2 < num4:
    print(f"{num2} es el número menor")
elif num3 < num1 and num3 < num2 and num3 < num4:
    print(f"{num3} es el número menor")
else:
    print(f"{num4} es el número menor")
print("Fin del programa")