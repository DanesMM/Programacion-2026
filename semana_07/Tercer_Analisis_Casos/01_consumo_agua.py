"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]
#consumos_litros = [120, 120, 120, 120, 120]

# TODO: Calcule el consumo total y el promedio diario.
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
reduccion = primer_dia - ultimo_dia
porcentaje_reduccion =(primer_dia - ultimo_dia) *100 / primer_dia

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje_reduccion >= 15:
    clasificacion = "Reducción alta"
elif porcentaje_reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"

# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
print(f"Consumo total: {consumo_total} L")
print(f"Promedio diario: {promedio_diario:.1f} L")
print(f"Ahorro: {reduccion} L")
print(f"Reducción: {porcentaje_reduccion:.0f} %")
print(f"Clasificación: {clasificacion}")
