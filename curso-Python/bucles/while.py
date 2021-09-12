# Bucle While

import math

numero = int(input("Digite un numero: "))

while numero < 0:
    print("ERROR! deberia ser un numero mayor a 0")
    numero = (int(input("Digite un numero: ")))

print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")