conjunto = set() # esto es un conjunto 
# eso se puede hacer solo luego de escribir lo anterior
conjunto = {1,2,3,"seis","siete",8,9}
print(conjunto)
conjunto.add(7) #agrego elemento
conjunto.add("cadena") #agrego elemento
print(conjunto)
conjunto.discard(1) #borro elemento
print(conjunto)
conjunto.clear() #borro elementos
print(conjunto)

print(3 in conjunto) #busco
print(1 in conjunto) #busco
print(1 not in conjunto) #busco

print("---------------------------")
print("---------------------------")
print("---------------------------")

a = frozenset({1,2,3})
b = {3,4,5}

print(a == b) 
print(len(a))
print(len(b))

c = a | b #union de 2 conjuntos
print(c)

c = a & b 
print(b) # interseccion

c = a - b # diferencia
print(c)

c = a ^ b #diferencia simetrica
print(c)

#subconjunto 
print(a.issubset(c))

#superconjunto
print(c.issuperset(a))

#disconexos
print(a.isdisjoint(b))

#hacerlos inmutables
# con ( frozenset({conjunto})) no se puede hacer .add
print(a)