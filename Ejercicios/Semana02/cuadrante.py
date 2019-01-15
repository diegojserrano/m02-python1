x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))


if x == 0 and y == 0:
    ubicacion = "Origen"
elif x == 0:
    ubicacion = "Eje de las abcisas"
elif y == 0:
    ubicacion = "Eje de las ordenadas"
else:
    if x > 0:
        if y > 0: ubicacion = "Cuadrante 1"
        else: ubicacion = "Cuadrante 4"
    else:
        if y > 0: ubicacion = "Cuadrante 2"
        else: ubicacion = "Cuadrante 3"

print("El punto esta en el", ubicacion)
