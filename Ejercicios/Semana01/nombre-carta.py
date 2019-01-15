numero = int(input("Ingrese el número de la carta, entre 1 y 12:"))

if numero == 1:
    nombre_carta = "As"
elif numero == 10:
    nombre_carta = "Sota"
elif numero == 11:
    nombre_carta = "Caballo"
elif numero == 12:
    nombre_carta = "Rey"
else:
    nombre_carta = str(numero)
    
print("Ud. tiene un", nombre_carta)