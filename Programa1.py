num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))


if num1 > num2 :
    print(f"{num1} es el número mayor\n{num2} es el número menor")
elif num1 == num2:
    print(f"{num1} es igual a {num2}")
else:
    print(f"{num2} es el número mayor\n{num1} es el número menor")
print("Fin del programa")