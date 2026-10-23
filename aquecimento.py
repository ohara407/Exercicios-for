saldo = 1500
while True:
    opcao = input("O que deseja realizar? \n1 - Sacar; \n2 - Depositar; \n3 - Sair\n").lower()
    
    if opcao == "sacar" or opcao=="1":
        sacar = float(input("Informe o valor a ser sacado: "))
        
        if sacar > saldo or sacar <=0:
            print("Saldo Insuficiente, Tente Novamente: ")
        else:
            print("Sacando")
            saldo -= sacar
            print(f"Valor atual da conta: {saldo}")
    elif opcao == "sair" or opcao =="3":
        print("Saindo")
        break
    elif opcao == "depositar" or opcao == "2":
        deposito = float(input("Informe o valor a ser depositado: "))
        saldo += deposito
        print("Valor Atual com o Deposito: ", saldo)
    else:
        print("Opção inválida !")