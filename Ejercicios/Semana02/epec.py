categoria = int(input("Ingrese la categoría del cliente: "))
consumo = int(input("Ingrese la cantidad de kw/h consumidos: "))

if categoria == 1:
    tarifa = 0.28
elif categoria == 2:
    tarifa = 0.32
else:
    tarifa = 0.41

subtotal = consumo * tarifa
iva = subtotal * 0.21
total = subtotal + iva

print("El total a pagar es de $:", total)

if categoria == 2 or categoria == 3:
    print("El IVA es de $:", iva)

