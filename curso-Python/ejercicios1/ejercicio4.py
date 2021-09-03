'''
    Hacer un programa para ingresar el radio de un circulo 
    y se reporte su area y la longitud de la circunferencia
'''
from math import pi

radio = float(input("radio > "))

area = pi * radio**2
circunferencia = 2 * pi * radio

'''
    Se puede cambiar la forma de hacer de esta:
    area = math.pi * radio**2
    circunferencia = 2 * math.pi * radio

    para acortar decimales usamos {dato:.xf}
    x = numero de decimales
'''
print(f"area -> {area:.2f} \nlongitud -> {circunferencia:.2f}")