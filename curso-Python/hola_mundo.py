print("Hola mundo!")
print("Hola \n mundo con salto de linea!")
print("---------------------------------")

numero = 10
print(numero)
print(type(numero))
print("---------------------------------")

decimal = 10.45
print(decimal)
print(type(decimal))
print("---------------------------------")

cadena = 'Caracteres o cadena de texto con comillas dobles o simples'
print(cadena)
print(type(cadena))
print("---------------------------------")

comillas = 'Caracteres o cadena de "texto con comillas" dobles o simples'
print(comillas)
print(type(comillas))
print("---------------------------------")

valor = True
print(valor)
print(type(valor))
print("---------------------------------")

valor = False
print(valor)
print(type(valor))
print("---------------------------------")

num1 = 3
num2 = 3.5
suma = num1+num2
print("El resultado es: ",suma)
print("---------------------------------")

# comentarios asi con #
# python permite el tipado dinamico

''' 
    Esto es un comentario multilinea
'''

# Operadores
num1 = 13
num2 = 2
resultado = num1 + num2 
print(resultado)
resultado = num1 - num2
print(resultado) 
resultado = num1 * num2
print(resultado)
resultado = num1 / num2
print(resultado)
resultado = num1 // num2
print(resultado)
print("--------------------------------")
# modulo
resultado = num1 % num2
print(resultado)

#potencia
resultado = num1 ** num2
print(resultado)

# Operadores relacionales (<,>, =,!=, >=, >=) devuelve un valor boolean

resultado = 10 > 10
print(resultado)
resultado = 10 < 10
print(resultado)
resultado = 10 >= 10
print(resultado)
resultado = 10 <= 10
print(resultado)
resultado = 10 != 10
print(resultado)
resultado = 10 == 10
print(resultado)

a = 20
b = 10
c = 30

resultado = a+b == c
print(resultado)

# Operadores Logicos (and, or, not) devuelve un valor boolean

resultado = (((a == c) or (b == c)) and ((c > a) or (c < a)))
print(resultado)

# Prioridad de los operadoes en general
'''
    Primero son los ()
    Segundo es la exponenciacion ** 
    *, /, mod, not 
    +, -, and
    >, <, ==, >=, <=, !=, or     
'''

# Opreadores de asignacion 

a = 0
a += 1
a -= 5
a *= 3
a /= 2
a **= 1
a %= 6

# Salidas 

nombre = 'Nicolás'
edad = 23 
print("Hola mi nombre es {} y tengo {}".format(nombre,edad))
print("Hola mi nombre es", nombre,"y tengo ", edad," años")
print(f"Hola {nombre} tienes {edad} años") #esta es la mejor forma, facil y rapida
print("--------------------------------")

# Entrada de datos 

nombre = input("digite su nombre: ") #Asi guardo una cadena

# Asi guardo una cadena {edad = input("Digite su edad: ")}
edad = int(input("Digite su edad: "))
sueldo = float(input("Digite su edad: "))
print(f"Hola {nombre} tu edad es {edad} años")

# Funciones integradas - para hacer conversion entre tipos de datos

n = str(21) # se pasa un valor numerico a cadena
print(n)

#valor entero a binario
n = bin(21) 
print(n)
# valor entero a hexadec
n = hex(21) 
print(n)
# bin a entero 
n = int("0b1010", 2)
print(n)
print("--------------------------------")

# Valor absoluto
n = abs(-8)
print(n)
# redondear
n = round(5.6)
print(n)
# cuenta Caracteres
n = len("Nicolas") 
print(n)
print("--------------------------------") 