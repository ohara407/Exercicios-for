"""
contador = 0

while contador < 5:
    print(f"Número: {contador}")
    contador = contador + 1
  """  
"""
contador = 0

x = 0
while x<5:
    print(x)
    x=x+1
else:
    print("Acabou")
"""
"""
contador  = 0
while True:
    print(contador)
    contador +=1
    if contador >= 3:
        break
"""
"""
notas = 0
qnt_notas_info = 0
while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if (nota==-1):
        break
    notas = notas + nota
    qnt_notas_info = qnt_notas_info+1
if qnt_notas_info > 0:
    media = notas/qnt_notas_info
    print(f"Quantidade de notas informadas: {qnt_notas_info}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota informada")
"""
"""
nota = float(input("Digite uma nota entre 0 a 10: "))

while nota < 0 or nota > 10:
        print("Nota inválida")
        nota = float(input("Digite uma nota entre 0 e 10: "))
else:
    print("Nota Valida")
"""
"""
notas = 0
qnt_notas_info = 0
while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if (nota==-1):
        break
    notas = notas + nota
    qnt_notas_info = qnt_notas_info+1
if qnt_notas_info > 0:
    media = notas/qnt_notas_info
    print(f"Quantidade de notas informadas: {qnt_notas_info}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota informada")   
""" 
"""
while True:
        qtd_turmas = int(input("Digite a quantidade de turmas: "))
        if qtd_turmas > 0:
            break
        print("Por favor, digite um número maior que zero.")
total_alunos = 0
turma_atual = 1
while turma_atual <= qtd_turmas:
        alunos = int(input(f"Digite a quantidade de alunos da turma {turma_atual}: "))
        
     
        if 0 <= alunos <= 40:
            total_alunos += alunos
            turma_atual += 1
        else:
            print("Erro: A turma não pode ter menos de 0 ou mais de 40 alunos. Tente novamente.")
media = total_alunos / qtd_turmas
print(f"\nTotal de turmas: {qtd_turmas}")
print(f"Total de alunos: {total_alunos}")
print(f"Média de alunos por turma: {media:.2f}")
"""
"""
senha = input("Crie sua senha: ")
rsenha = input("Digite novamente sua senha")
while rsenha != senha:
    print("Senhas Diferentes")
    print("Digite Novamente sua senha: ")  
    rsenha = input("Digite novamente sua senha: ")
else: 
    print("Senha criada")
"""
"""
numeros = 0
while True:
    numero = int(input("Digite numeros inteiros. Dite 0 para sair: "))
    if (numero==0):
        break
    numeros = numeros + numero
    

print(f"Soma dos Numeros: {numeros}")
"""
"""""
# 6. Crie um programa que receba um número inteiro e imprima sua tabuada de 1 a 10.

# Inputs: o numero inteiro
# Criterio de reptição: Rodar dez vezes, *contador*
# O que acontece a cada repetição? : Ele multiplica e mostra o resultado

n = int(input("Digite um número: "))
contador = 1
while contador <= 10 :
    print(f"{n} x {contador} = {n*contador}")
    contador = contador + 1


# 7. Escreva um programa para contar o número total de dígitos em um número inteiro
# dado usando um laço while.  (Dica utilize o operador de divisão inteira).
# Utilize um laço while que continue enquanto o número não for zero.
# Em cada iteração, divida o número por 10 (para remover o último dígito)
# e incremente um contador.

# Inputs: Um numero inteiro
# Critério de repetição: É o tamanho do número, contador
# O que ele vai fazer a cada loop ? : Diminuir os digitos do meu número

n = int(input("Digite um número: "))
contador = 0
while n != 0:
    n = n//10
    contador = contador + 1
else:
    print(f"O número de digitos é {contador}")
assignment
Atividade: "Atividade 6 - Desafio de ATM"
Lucas Cardoso postou uma nova atividade: Atividade 6 - Desafio de ATM
Criado em: OntemOntem


while True:
    opcao = input("O que desjea realziar? \n1 - Sacar; \n2 - Depositar; \n3 - Sair").lower()
    if opcao == "sacar":
        # Fazer a logica de saque
    elif opcao == "depositar":
        # Fazer a lógica de depositar
    elif opcao == "sair":
        print("Finalizando o sistema")
        break
    else:
        print("Opção inválida !")
    """
    


            
            
    

