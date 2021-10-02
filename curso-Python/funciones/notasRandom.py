import random
import math
import statistics as stats

def notasAleatorias(n):
    lista=[0]*n
    for i in range(n):
        lista[i]=random.randint(1,7)
    return lista

n = int(input('n° de notas -> '))

aleatorios=notasAleatorias(n)
print(aleatorios)
aleatorios.sort()
print("notas ordenadas")

print(aleatorios)
promedio = stats.mean(aleatorios)
moda = stats.mode(aleatorios)
mediana = stats.median(aleatorios)

print(f"Media -> {promedio:.2f}")
print(f"Moda -> {moda:.2f}")
print(f"Mediana -> {mediana:.2f}")
