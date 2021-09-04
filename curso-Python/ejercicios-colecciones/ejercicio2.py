'''
Crea dos listas en als que se almacenen elementos,
sin repetir.
'''

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,5,8,9,10]

# elementos de ambas listas
lista3 = list(set(lista1+lista2))