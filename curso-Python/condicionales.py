# Condicionales
numero = int(input("número => "))
if numero >= 0:
    print(f"El número {numero} es mayor o igual que 0")
else:
    print(f"El número {numero} es menor que 0")
print("Fin de condicion")

if numero == 0:
    print("El numero es cero")
elif numero > 0:
    print(f"El numero es distinto de cero {numero}")
else:
    print("Dato no valido")

print("-------------------------------------")

# Condicionales combinados

edad = int(input("Que edad tienes -> "))

if edad > 0 and edad < 100: # se puede acortar con 0<edad<100
    print("Edad correcta")
    if edad >= 18: 
        print("Es mayor de edad")
else:
    print("La edad es incorrecta")