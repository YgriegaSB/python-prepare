n1 = int(input("n1 => "))
n2 = int(input("n2 => "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos son pares")
elif n1 % 2 == 1 and n2 % 2 == 1:
    print("Ambos son impares")
elif n1%2==1 and n2%2==0:
    print(f"{n1} es impar y {n2} es par")
else:
    print(f"{n1} es par y {n2} es impar")





