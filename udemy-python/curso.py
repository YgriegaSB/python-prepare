mivar = "Hola mundo"
print(mivar)

x = 100 # entero
y = 2 # entero
z = x + y

c = 10.5 # float

print(z)

# Direcciones de memoria
print ( id(z) )
# saber tipo 
z: str = "string"
print( type(z) )

print( type(x) ) 

x = True # o False BOOLEAN

texto = "Aerosmith"
print("Hola " + texto)
print(f"Hola {texto}" + " es lo mejor")
print(f"Hola {texto}", "es lo mejor")

#ejercicio como estuvo tu dia
cali = int(input("Como estuvo tu día (1 al 10): "))
print(f"Tu día estuvo de: {cali}")

# datos libro
titulo = input("Proporciona el titulo: ")
autor = input("Proporciona el autor: ")
print(f"{titulo} fue escrito por {autor}")

# Rectangulo
alto = float(input("Proporciona el alto del rectangulo: "))
ancho = float(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto+ancho)*2
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

print("-----------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------------

# par  o impar

num = int(input("Ingrese un numero: "))
if num%2 == 0:
    print("es un numero par")
else:
    print("es un numero impar")

