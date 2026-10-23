n = int(input("Informe a quantidade de pessoas que irá apresentar a idade: "))


beta = 0
alfa = 0
g_z = 0
g_y = 0
g_x = 0
baby = 0
silent = 0

for i in range(n):
    print(f"\nPessoa {i + 1}")
    idade = int(input("Idade: "))
    
    
    if idade <= 1:
        beta += 1
    elif idade >= 2 and idade <= 14:
        alfa += 1
    elif idade >= 15 and idade <= 29:
        g_z += 1
    elif idade >= 30 and idade <= 45:
        g_y += 1
    elif idade >= 46 and idade <= 61:
        g_x += 1
    elif idade >= 62 and idade <= 80:
        baby += 1
    else:
        silent += 1


print("\n=== RESULTADO TOTAL ===")
print(f"Geração Beta: {beta}")
print(f"Geração Alfa: {alfa}")
print(f"Geração Z: {g_z}")
print(f"Geração Y: {g_y}")
print(f"Geração X: {g_x}")
print(f"Geração Baby Boomers: {baby}")
print(f"Silent Generation: {silent}")

#Numa eleição existem três candidatos: Faça um programa que peça o número total de eleitores. Peça para cada eleitor
#votar e ao final mostrar o número de votos de cada candidato

eleitores = int(input("Informe a quantidade de eleitores: "))
cand_1 = 0
cand_2 = 0
cand_3 = 0
for i in range(eleitores):
    voto = print("Informe a quantidade de votos: ")
    
    
    
    
    
total_pessoas = int(input("Informe a quantidade total de pessoas no grupo: "))

total_masculino = 0
total_feminino = 0

for i in range(total_pessoas):
    print(f"\n--- Pessoa {i + 1} ---")
    
    while True:
        sexo = input("Informe o sexo (M/F): ").strip().upper()
        if sexo == 'M':
            total_masculino += 1
            break
        elif sexo == 'F':
            total_feminino += 1
            break
        else:
            print("Entrada inválida! Por favor, digite 'M' para masculino ou 'F' para feminino.")

print("final")
print(f"Total de pessoas do sexo masculino: {total_masculino}")
print(f"Total de pessoas do sexo feminino: {total_feminino}")


total_homens = 0
soma_idade_homens = 0

total_mulheres = 0
soma_idade_mulheres = 0

soma_idade_grupo = 0
TOTAL_PESSOAS = 10

for i in range(TOTAL_PESSOAS):
    print(f"\n--- Dados da Pessoa {i + 1} ---")
    
    idade = int(input("Digite a idade: "))
    soma_idade_grupo += idade
    
    while True:
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        if sexo == 'M':
            total_homens += 1
            soma_idade_homens += idade
            break
        elif sexo == 'F':
            total_mulheres += 1
            soma_idade_mulheres += idade
            break
        else:
            print("Entrada inválida! Use apenas 'M' ou 'F'.")

media_grupo = soma_idade_grupo / TOTAL_PESSOAS
media_homens = (soma_idade_homens / total_homens) if total_homens > 0 else 0
media_mulheres = (soma_idade_mulheres / total_mulheres) if total_mulheres > 0 else 0

print("FInal")
print(f"Idade média do grupo: {media_grupo:.1f} anos")

if total_homens > 0:
    print(f"Idade média os homens: {media_homens:.1f} anos (Total: {total_homens})")
else:
    print("Nenhum homem foi registrado no grupo.")

if total_mulheres > 0:
    print(f"Idade média das mulheres: {media_mulheres:.1f} anos (Total: {total_mulheres})")
else:
    print("Nenhuma mulher foi registrada no grupo.")
