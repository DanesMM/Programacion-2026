"""CREE UN PROGRAMA EN PYHTON QUE:
    - Cree una lista con 3 calificaciones decimales y la muestre.
    - Cambie una calificación utilizando su posición.
    - Cree otra lista con 2 calificaciones adicionales y una ambas listas.
    - Ordene las calificaciones con sort().
    - Muestre la nota menor, la mayor y la cantidad total usando min(), max() y len().
    - Solicite una nueva calificación con input() y agréguela con append().
    - Inserte una calificación en la posición 1 usando insert().
    - Elimine una calificación con remove().
    - Verifique con if e in si una nota específica se encuentra en la lista.
    - Muestre la lista final de calificaciones.
    - Importante: convierta las notas ingresadas por el usuario utilizando float().
"""
#[] {} ><
#Listas de Calificaciones:
#					0		1		2
calificaciones = [98,19 , 99.52, 73.56]
calificaciones[1] = 86.93
calificaciones_2 = [60.11, 86.95]
general = calificaciones + calificaciones_2
general.sort()
print("NOTAS GENERALES: ", min(general) , max(general))
print("Estudiantes Calificados: " , len(general))

nueva_nota = float(input("Ingrese Nueva Calificación: "))
general.append(nueva_nota)
print(general)

general.remove(min(general))
print(general)

if 70.43 in general:
    print("70.43 sí está en las calificaciones")
else:
    print("70.43 no está en las calificaciones")


