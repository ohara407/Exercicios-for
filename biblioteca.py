biblioteca = {}
while True:
    print("\nMENU BIBLIOTECA")
    print("1. Cadastrar um livro")
    print("2. Pedir livro emprestado")
    print("3. Devolver livro")
    print("4. Consultar lista de livros emprestados")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        livro = input("Digite o nome do livro que deseja cadastrar: ")    
        if livro in biblioteca:
            print("Erro: Este livro já está cadastrado!")
        else:
            biblioteca[livro] = "Disponível"
            print(f"Livro '{livro}' cadastrado com sucesso!")
    elif opcao == "2":
        livro = input("Digite o nome do livro que deseja pegar emprestado: ")
        if livro in biblioteca:
            if biblioteca[livro] == "Disponível":
                biblioteca[livro] = "Emprestado"
                print(f"Empréstimo do livro '{livro}' realizado com sucesso!")
            else:
                print("Este livro já está emprestado no momento.")
        else:
            print("Erro: Livro não encontrado na biblioteca.")
    elif opcao == "3":
        livro = input("Digite o nome do livro que deseja devolver: ")
        if livro in biblioteca:
            if biblioteca[livro] == "Emprestado":
                biblioteca[livro] = "Disponível"
                print(f"Livro '{livro}' devolvido com sucesso!")
            else:
                print("Este livro já consta como disponível na biblioteca.")
        else:
            print("Erro: Livro não encontrado.")
    elif opcao == "4":
        print("\nLIVROS EMPRESTADOS")
        nenhum = True
        for livro, status in biblioteca.items():
            if status == "Emprestado":
                print(f"- {livro}")
                nenhum = False
        if nenhum:
            print("Nenhum livro emprestado no momento.")
    elif opcao == "5":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")