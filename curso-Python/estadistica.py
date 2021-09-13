import math
import statistics as stats

datos = []
contRelleno = 1
cont = 0
num = int(input("\t --> ¿Cuantos digitos piensa ingresar? <-- \n ==> "))

while contRelleno == 1:   
    dato = int(input("Digite un numero para el arreglo: "))
    datos.append(dato)
    cont += 1
    if cont == num:
        print(datos)
        print("\t Media")
        print(f"la media de los datos ingresados es: {stats.mean(datos):.2f}")
        print("\t Moda")
        print(f"La Moda de los datos ingresados es: {stats.mode(datos)}")
        print("\t Mediana")
        print(f"La mediana de los datos es: {stats.median(datos):.2f}")
        contRelleno = 0
