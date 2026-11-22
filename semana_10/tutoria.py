import pandas as pd

datos = {
    "nombre": ['Daniel', 'Moises', 'Diana', 'Jimena', 'Emanuel'],
    "edad": [16, 14, 14, 15, 13],
    "nota": [90, 96, 85, 62, 70]
}

estudiantes = pd.DataFrame(datos) #int("18")

print(estudiantes)

print(estudiantes.info()) #Versión Mejorada del print(type)
print("\nColumnas: " , estudiantes.columns)

print(estudiantes["nombre"])

print("\nNotas: \n", estudiantes["nota"])
print("Nota Menor: ", estudiantes["nota"].min())
print("Nota Mayor: ", estudiantes["nota"].max())
print("Nota Promedio: " , estudiantes["nota"].mean())

print("\nEdad: \n", estudiantes["edad"])
print("Edad Menor: ", estudiantes["edad"].min())
print("Edad Mayor: ", estudiantes["edad"].max())
print("Edad Promedio: " , estudiantes["edad"].mean())
