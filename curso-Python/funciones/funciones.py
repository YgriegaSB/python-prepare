# Funciones
'''
    Syntaxis:

    def nombre_funcion():
        Instrucciones de la funcion
        return(opcional)

    def nombre_funcion(parametros):
        Instrucciones de la funcion
        return(opcional)
'''


def suma():
    num1 = int(input('n1 -> '))
    num2 = int(input('n2 -> '))
    resultado=num1+num2
    print(resultado)

suma()

print("-------------------------------")
def resta(n1,n2):
    print(n1-n2)

resta(21,1)

print("-------------------------------")
def multi(num1, num2):
    resultado=num1*num2
    return resultado

'''
    para imprimir se debe colocar:
        print(funcion(datos))
'''
print(multi(5,10))

# Variable
almacena = multi(2,4)
print("------------------")
print(almacena)

# Python pasa valores por referencia


