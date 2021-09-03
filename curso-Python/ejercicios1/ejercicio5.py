'''
    Una tienda ofrece el 15% sobre el total  de la compra 
    y un cliente desea saber cuanto debera pagar finalmente
    por su compre.
'''

total = float(input("Total => "))
descuento = total * 0.15
final = total - descuento
print(f"Descuento => ${descuento}")
print(f"P. Final => ${final:.2f}")