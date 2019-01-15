votos1 = int(input("Ingrese los votos del primer candidato:"))
votos2 = int(input("Ingrese los votos del segundo candidato:"))

total = votos1 + votos2

porcentaje1 = votos1 * 100 / total
porcentaje2 = votos2 * 100 / total

if porcentaje1 > porcentaje2:
    ganador = "Candidato 1"
else:
    ganador = "Candidato 2"

print("Porcentaje de votos del primer candidato:", porcentaje1, "%")
print("Porcentaje de votos del segundo candidato:", porcentaje2, "%")
print("Ganó el", ganador)
