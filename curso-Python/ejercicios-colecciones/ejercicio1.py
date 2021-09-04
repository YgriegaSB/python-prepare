'''
programa donde tenga una lista y que elimine 
los elemntos repetidos, por ultimo mostrar lista
'''

lista = ["nicolas", "alejandro", "alice", "nicolas"]
print(lista)
#conjunto = set(lista)
#lista = list(conjunto)
lista = list(set(lista))
print(lista)