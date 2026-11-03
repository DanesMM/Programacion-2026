"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
print("REGISTROS DE SOPORTE UNIVERSITARIO")
print ("-" * 40)

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
control_casos = len(incidencias)
minutos_totales = 0
conteo_categorias = {
    "Acceso": 0, 
    "Equipo": 0,
    "Red": 0
    }

provincias = set()
pendientes = 0
urgentes = []
caso_mas_largo = ("", 0)

for incidencia in incidencias:
    minutos_totales += incidencia["minutos_atencion"]
    conteo_categorias[incidencia["categoria"]] += 1

    if not incidencia["resuelto"]:
        pendientes += 1
        provincias.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))

    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])

promedio = minutos_totales / len (incidencias)

print(f"Cantidad de Casos: {control_casos}")
print(f"Total de Minutos: {minutos_totales} minutos.")
print(f"Promedio de Minutos: {promedio:.0f} minutos.")

print(f"\nConteo por Categoría:")
for categoria, cantidad in conteo_categorias.items():
    print(f"  {categoria}: {cantidad} casos.")

print(f"\nCantidad de Pendientes: {pendientes} casos.")
print(f"Provincias con Pendientes: {provincias}")

print(f"\nCasos Urgentes: {urgentes}")
print(f"Caso más Largo: {caso_mas_largo}")

print(f"\n¿Hay Pendientes en San Jose?: {'San Jose' in provincias}")