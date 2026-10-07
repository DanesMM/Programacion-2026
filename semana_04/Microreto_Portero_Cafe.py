"""Microreto: el portero del café."""

energia = int(input("Cuanta energía tienes de 0-100?: ")) 
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() =="si"

#Proceso
if(energia <30 and not(trae_cafe)):
    mensaje = "Acceso Denegado: Necesitas dormir o tomar café."
elif(energia >= 30 or (trae_cafe)):
    mensaje = "Acceso Permitido: pasa, pero comparte café."
else:
    mensaje = "El guarda está confundido, revisa las respuestas."
print(mensaje)

#print("Tipo", type(trae_cafe))
#print("Trae café: ", trae_cafe)
#mensaje = "Completa las reglas del portero."

# TODO: usa and para detectar energía baja sin café.
# TODO: usa or para permitir energía suficiente o café.
# TODO: escribe mensajes claros para cada resultado.

#<>=