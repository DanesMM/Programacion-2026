#AUTOR: DANIEL MARTINEZ      
      #0		1		2
producto = ["Café", 5000, 20]
print("ANALISIS PROMOCION CAFE")
print("-" * 35)

print("PRODUCTO: ", producto[0])
print(f"Precio Actual: ₡, {producto[1]:,.2f}")
print("Unidades Actuales: " , producto[2])

ingreso_actual = producto[1] * producto[2]
print(f"Ingreso Actual: ₡, {ingreso_actual:,.2f}\n")

print("Descuento: 15%")
porcentaje_aumento = 20
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento
print(f"Precio Promocional: ₡{precio_promocional: ,.2f}")
print(f"Aumento Esperado en Ventas: {porcentaje_aumento}%")


ingreso_actual = producto[1] * producto[2]
unidades_proyectadas = (producto[2] * porcentaje_aumento / 100) + producto[2]
print(f"Unidades Proyectadas: {unidades_proyectadas:.0f}\n")

ingreso_proyectado = (precio_promocional * unidades_proyectadas)
diferencia = (precio_promocional * unidades_proyectadas) - ingreso_actual
print(f"Ingreso con Promoción: ₡{ingreso_proyectado: ,.2f}")
print(f"Diferencia: ₡{diferencia:,.2f}\n")

if ingreso_proyectado > 0:
    print("RECOMENDACIÓN: Lanzar Promoción")
else:
    print("NO ES RENTABLE, no lanzar Promoción")