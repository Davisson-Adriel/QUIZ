from funciis import*

print("Hola querido usuario")
print("--------------------")

while True:

    mostrar_menu()
    opc=int(input("Digite el numero de acuerdo a su elecciòn: "))

    if opc==1:
        numeros_alma.clear()
        while True:

            limit=int(input("Digite el rango limite superior: "))

            if limit <= 2:
                print("Rango invalido")
            else:

                for x in range(2,limit+1):
                    deter_primo(x)
                print(numeros_alma)

                gemelos=[]

                
                break


    elif opc==2:
        
        
        numeros_alma.clear()
        while True:
            

            limit=int(input("Digite el rango limite superior: "))

            if limit <= 10:
                print("Rango invalido")
            else:

                for x in range(2,limit+1):
                    deter_primo(x)
                print("------------------------------")
                palindro(numeros_alma)
                print("------------------------------")
                
                break

    elif opc==3:
        print("Hasta Luego vuelva pronto")
        break
    else:
        print("Opciòn invalida")




