num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))
num3 = int(input("Dame un último número entero: "))

if num1 < num2 and num1 < num3:
    print(f"{num1} es el número menor")
elif num2 < num1 and num2 < num3:
    print(f"{num2} es el número menor")
else:
    print(f"{num3} es el número menor")
print("Fin del programa")