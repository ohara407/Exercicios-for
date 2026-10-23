saldo = 1500
while True:
    opcao = input("O que desjea realziar? \n1 - Sacar; \n2 - Depositar; \n3 - Sair\n").lower()
    
    if opcao == "sacar":
        sacar = float(input("Informe o valor a ser sacado: "))
        
        if sacar > saldo:
            print("Saldo Insuficiente, Tente Novamente: ")
        else:
         print("Sacando")
         saldo -= sacar
        print(f"Valor atual da conta: {saldo}")
    elif opcao == "sair" or opcao =="3":
        print("Saindo")
        break