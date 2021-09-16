# par o impar

def parimpar(num):
    resultado=num%2
    if resultado==0:
        print(f'{num} es par \n')
    else:
        print(f'{num} es impar \n')

print('En que numero estas pensando?')
n = int(input('n° -> '))
parimpar(n)

cont = 0 

while cont==0:
    print("\t Deseas añadir otro")
    res = str(input("S or n -> "))

    if res == "s" or res == "S":
        n = int(input('n° -> '))
        parimpar(n)
    else:
        print("Finalizando...........")
        cont = 1
