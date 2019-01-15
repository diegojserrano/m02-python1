a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))

if a != b:
    if a > b:
        mayor = a
    else:
        mayor = b
    print("El mayor es:", mayor)

else:
    print("Los números son iguales")

