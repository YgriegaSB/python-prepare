# cajero 
#ingresar dinero
#retirar
#mostrar
#salir
saldo = 1000
i = 0
while i == 0:
    print("\tCAJERO AUTOMATICO")
    print("Opciones:")
    print("1->Ingresar Dinero")
    print("2->Retirar Dinero") 
    print("3->Mostrar Saldo") 
    print("4->Salir")
    opcion = int(input("Digite la opcion que desea: 1,2,3,4: "))
    if opcion == 4:
        print("------------------------------------\n")
        print("\tSaliendo....\n")
        print("------------------------------------\n")
        i = 1
    elif opcion == 1:
        print(f"Tu saldo es de {saldo}")
        monto = float(input("monto -> "))
        saldo += monto
        print("------------------------------------\n")
        print(f"\tSaldo: {saldo}\n")
        print("------------------------------------\n")
    elif opcion == 2: 
        print(f"Tu saldo es de {saldo}")
        monto = float(input("monto -> "))
        if monto > saldo:
            print("\n-->No cuentas con la cantidad suficiente<--")
        else:
            saldo -= monto
        print("------------------------------------\n")
        print(f"\tSaldo: {saldo}\n")
        print("------------------------------------\n")
    elif opcion == 3:
        print("------------------------------------\n")
        print(f"\tSaldo: {saldo}\n")
        print("------------------------------------\n")
    else:
        print("------------------------------------\n")
        print("\topcion invalida!!!!!!\n")
        print("------------------------------------\n")