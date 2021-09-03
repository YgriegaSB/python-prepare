# pide 3 números, imprime el mayor

n1 = int(input("n1 ==> "))
n2 = int(input("n2 ==> "))
n3 = int(input("n3 ==> "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} es el mayor")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} es el mayor")
else:
    print(f"{n3} es el mayor")

'''
    Una forma más "corta de escribirlo

    if n1 >= n2 >= n3:
        print(f"{n1} es el mayor")
    elif n2 >= n1 >= n3:
        print(f"{n2} es el mayor")
    else:
        print(f"{n3} es el mayor")
'''