def obtener_persona(activo = False):
    #              0      1         2          3
    lista = ["Daniel", 26, "Programación", activo]
    tupla = ("Daniel", 26, "Programación", activo)

    return (lista)
    #             -4     -3         -2         -1

persona = obtener_persona(True)

print("Nombre: ", persona[0])
print(f"Edad: ", persona[1], "años")
print("Estudiante de: ", persona [2])
print("Tipos Estructura: ", type(persona))
print("Estudiante Activo: ", persona[3])


#Parte interesante de las tuplas, lo que lo diferencia de las listas.
#Solo se return a tuplas.
#los parámetros se envian por tuplas.
#En memoria a la tupla se le da una memoria fija.
#Las listas son más dinámicas.
#Las Tuplas siempre se usan para el envío de datos y el returno de datos.
#¿Cuándo usaría una tupla? Podemos usarla cuando declaramos valores constantes.