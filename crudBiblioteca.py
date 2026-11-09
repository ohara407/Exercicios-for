biblioteca = {}
while True:
    print("\nMenu Biblioteca")
    print("1 - Cadastrar um Livro")
    print("2 - Pedir um Livro")
    print("3 - Devolver um Livro")
    print("4 - Consultar uma Lista de Livros Emprestados")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    if opcao == 1:
        titulo = input("Digite o titulo do livro para cadastrar: ").strip()
        
        if titulo in biblioteca:
            print(f"Erro: O livro '{titulo}' já está cadastrado!")
        else: 
            biblioteca[titulo] = "disponivel" 
            