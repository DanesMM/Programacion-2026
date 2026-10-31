"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
#asistencias = [240, 240, 240, 240, 240]
capacidad = 300

total = 0
capacidad_sobre_70 = 0

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for a in asistencias:
    total += a
    if a > 0.7 * capacidad:
        capacidad_sobre_70 += 1

# TODO: Calcule el promedio y su porcentaje de ocupación del promedio.
promedio = total / len(asistencias)
porcentaje_ocupacion = promedio * 100/ capacidad
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    estado = "Ocupación Alta"
elif porcentaje_ocupacion >= 50:
    estado = "Ocupación Media"
else:
    estado = "Ocupación Baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print(f"Total: {total}")
print(f"Promedio: {promedio:.0f}")
print(f"Porcentaje de Ocupación: {porcentaje_ocupacion: .0f}%")
print(f"Cantidad de Bloques: {capacidad_sobre_70}")
print(f"Estado: {estado}")
