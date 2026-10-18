#Semana05_Repaso
#Listas
# [] {} ><
#			0			1		2		
frutas = ["Manzana", "Pera", "Uvas"]
print(frutas)
frutas[1] = "kiwi"
print(frutas)

temporada = ["Papaya", "Melón"]
frutas = frutas + temporada
frutas.sort()
print(min(frutas), max(frutas))
print("Cantidad: ", len(frutas))
print(frutas)

nueva_fruta = input("Ingrese una Fruta: ").strip().lower()
frutas.append(nueva_fruta)
print(frutas)
frutas.insert(1, "Sandia")
print(frutas)

frutas.remove("Melón")
print(frutas)