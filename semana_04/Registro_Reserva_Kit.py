#Solución Misión Kit Seguro
#Autor: Daniel Martínez M. Fecha 2026/10/06

nombre = input("Nombre: ").strip().upper()
kit = input("Tipo de Kit: ").strip().lower()
autorizacion = input("Tiene Autorización (si/no)?: ").lower().strip() =="si"

try:
    cantidad = int(input("Ingrese la Cantidad: "))
except ValueError:
    print("Error Cantidad Inválida, asignada -1")
    cantidad = -1
    
try:
    dias = int(input("Días de Prestamo?: "))
except ValueError:
    print("Error Cantidad Inválida")
    dias = -1
 
resultado = "" 
if not nombre or not kit or cantidad <1 or dias <1 :
    resultado = "Registro Rechazado: Datos Inválidos"
elif autorizacion and cantidad <= 3 and dias <=7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}"
elif cantidad >3 or dias >7:
    resultado = "Solicitud enviada a revisión"
else:
    resultado = "Solicitud Rechazada: Se requiere autorización"
    
print(resultado)

# TODO: solicita los datos.
# TODO: limpia los textos.
# TODO: convierte los números con try.
# TODO: valida las entradas.
# TODO: aplica las reglas.
# TODO: muestra el resultado.
