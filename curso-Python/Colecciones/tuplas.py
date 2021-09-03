# las tupals son listas inmutables(no se modifica)

tupla = (4, "hola", 6.78, [1,2,3], 4)
print(tupla)
print(tupla[3])
print(tupla[1:])

print("-----------------------------------")

print(4 in tupla)
print(tupla.index(4))
print(tupla.count(4))

lista = list(tupla)
print(lista)
lista.append(23) #ahora puedo editar la tupla copiada en lista
print(lista)

#si tengo una lista y la quiero pasar a tupla tengo que usar tuple(variable)