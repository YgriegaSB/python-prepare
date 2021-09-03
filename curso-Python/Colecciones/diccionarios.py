# Diccionarios tambien aceptan distintos tipos de datos, 
# ademas de ponerle otras colecciones

# se almacena clave:valor
diccionario = {"Azul":"Blue", "Rojo":"Red", "Verde":"Green"}
print(diccionario)
print("----------------------------")
print(diccionario["Azul"])
print("----------------------------")
#agregar almacena
diccionario["Amarillo"] = "Yellow"
print(diccionario)
print("----------------------------")
#modificar
diccionario["Azul"] = "BLUE"
print(diccionario["Azul"])
print("----------------------------")
# Eliminar
del(diccionario["Azul"])
print(diccionario)

print("----------------------------")
print("----------------------------")
print("----------------------------")

personas = {"Nicolás":[23, 1.90], "José":[23, 1.75]} # con lista
print(personas)

print("----------------------------")
print("----------------------------")
print("----------------------------")

personas = {"Nicolás":{"edad":21, "estatura":1.90}}
print(personas)
print("--------------------------------------------------------------------------------")
# Diccionario part2
print("\tDiccionario Part2")

equipo = {10:"Alexis Sanchez", 1:"Claudio Bravo", 8:"Arturo Vidal", 27:"Pablo Aranguiz"}
print(equipo)
print(equipo[10])

#de esta forma evitamos un error en el programa 
print(equipo.get(30, "no existe un jugador con ese dorsal"))

#buscar
print(10 in equipo)

#mostrar claves
print(equipo.keys())
#mostrar valores
print(equipo.values())

#mostrar diccionario
print(equipo.items())
print(len(equipo))

#borrar
equipo.clear()
print(equipo)