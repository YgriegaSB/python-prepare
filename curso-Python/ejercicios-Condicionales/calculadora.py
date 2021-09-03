# calculadora suma(S,s), 
# Resta(R,r), Multi(M,m), Divi(D,d)

print ("Operaciones: \n ->Suma:S,s\n ->Resta:R,r\n ->Multi:M,m\n ->Divi:D,d")
operacion = input("Digitite la inicial de la operacion que desea realizar\n").lower() #puedes poner .upper() if x=="S"

if operacion=="s":
    print("->SUMA<-")
    n1 = float(input("num1 => "))
    n2 = float(input("num2 => "))
    resultado = n1 + n2
    print (resultado)
elif operacion=="r":
    print("->RESTA<-")
    n1 = float(input("num1 => "))
    n2 = float(input("num2 => "))
    resultado = n1 - n2
    print (resultado)
elif operacion=="m":
    print("->MULTIPLICACION<-")
    n1 = float(input("num1 => "))
    n2 = float(input("num2 => "))
    resultado = n1 * n2
    print (resultado)
elif operacion=="d":
    print("->DIVISION<-")
    n1 = float(input("num1 => "))
    n2 = float(input("num2 => "))
    resultado = n1 / n2
    print (resultado)
else:
    print("dato no valido")