"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) #Total de ventas semanal
cantidad_centro = len(ventas_centro) #Cantidad Días Registrados

promedio_centro = total_centro / cantidad_centro
menor_centro = min(ventas_centro) #Venta Mínima Centro
mayor_centro = max (ventas_centro) #Venta Máxima Centro

porcentaje_centro = total_centro * 100 / meta_centro
# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte) #Total de ventas semanal
cantidad_norte = len(ventas_norte) #Cantidad Días Registrados

promedio_norte = total_norte / cantidad_norte
menor_norte = min(ventas_norte) #Venta Mínima Norte
mayor_norte = max (ventas_norte) #Venta Máxima Norte

porcentaje_norte = total_norte * 100 / meta_norte

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
        estado_centro = "meta superada"
elif total_centro == meta_centro:
        estado_centro = "meta alcanzada"
else:
    estado_centro = "meta NO alcanzada"

if total_norte > meta_norte:
        estado_norte = "meta superada"
elif total_norte == meta_norte:
        estado_norte = "meta alcanzada"
else:
    estado_norte = "meta NO alcanzada"
# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_mayor_ventas = "Tienda del Centro"
elif total_norte > total_centro:
    tienda_mayor_ventas = "Tienda del Norte"
else:
    tienda_mayor_ventas = "Ambas Tiendas Tienen el mismo Total"
    
# TODO: presenta un reporte con etiquetas claras y f-strings.
print("COMPARACIÓN SEMANAL DE TIENDAS")
print("-" * 70)
print(f"Centro | total: ₡{total_centro: ,.2f} | meta ₡{meta_centro: ,.2f} | cumplimiento {porcentaje_centro: .0f}%")
print(f"Centro Logro: {estado_centro}\n")
print(f"Norte | total: ₡{total_norte: ,.2f} | meta ₡{meta_norte: ,.2f} | cumplimiento {porcentaje_norte: .0f}%")
print(f"Norte Logro: {estado_norte}\n")

print("Tienda con Mayor Ventas:" , tienda_mayor_ventas)

# TODO: escribe las tres conclusiones solicitadas en la guía.
