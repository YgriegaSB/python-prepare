# listas

lista = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(lista) #lista completa
print(lista[0]) #Un dato de la lista
print(lista[2:4]) #desde un punto de la lista a otro
print(lista[2:]) #desde un punto de la lista hasta el final
print(lista[:4]) #si dejas vacio se imprime desde el inicio

lista = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40,20.55,[1,2,3,4],True, False]
print(lista)
print(len(lista)) # Cantidad de elementos dentro de lista
print("\n ------------------------------------- \n")

numeros = [1,2,3,4,5,6,7]
print(numeros)
numeros.append(8) #agrego elemento al final de la lista
print(numeros)
numeros.insert(0,3) 
print(numeros)
'''
    numeros.insert(0,3) 
    asi agrego un elemento a una posicion 
    especifica primero posicion despues el valor
'''
numeros.extend([9,10,11])
print(numeros)
print("\n -------------------------------------------- \n")
lista3 = lista + numeros
print(lista3)
print("\n -------------------------------------------- \n")

# buscar un determinado elemente en lista
print(3 in numeros) #devuelve un boolean true or false
# buscar el indice de un elemento
print(numeros.index(3))
# Buscar cuantas veces se repite un elemento
print(numeros.count(3))

#eliminar elementos
numeros.pop()
print(numeros)
# eliminar elemento indicando indice
numeros.pop(0)
print(numeros)
# eliminar elemento indicando elemnto
numeros.remove(10)
print(numeros)
# Eliminar todos los elementos
numeros.clear()
print(numeros)
# voltear lista 
numeros.reverse()
print(numeros)
print("\n -------------------------------------------- \n")

# duplicar los elementos

numeros = [1,2,3,4,5,6,8,22,11]*2 # *n cantidad de veces
print(numeros)
# ordenar lista asendentemente
numeros.sort()
print(numeros)
print("\n -------------------------------------------- \n")
# Ordenar lista descendentemente
numeros.sort(reverse=True)
print(numeros)