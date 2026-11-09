for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    else:
        continue
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
    elif idade >= 81 and idade <= 101:
            sg += 1    
    else:
        print("idade invalida")


print("RESULTADO TOTAL")
print(f"Geração Beta: {beta}")
print(f"Geração Alfa: {alfa}")
print(f"Geração Z: {g_z}")
print(f"Geração Y: {g_y}")
print(f"Geração X: {g_x}")
print(f"Geração Baby Boomers: {baby}")
print(f"Silent Generation: {silent}")



qtd_eleitores = int(input("Informe a quantidade de eleitores: "))
cand_1 = 0
cand_2 = 0
cand_3 = 0
for i in range(qtd_eleitores):
    voto = int(input("Informe a quantidade de votos: "))
    if voto == 1:
        cand_1 += 1
    elif voto == 2:
        cand_2 += 1
    elif voto == 3:
        cand_3 += 1
        
print(f"os votos foram distribuidos: \nCandidato 1 {cand_1} votos \nCandidato 2 {cand_2} votos \nCandidato 3 {cand_3} votos ")
    
    
    
    
    
total_pessoas = int(input("Informe a quantidade total de pessoas no grupo: "))

total_masculino = 0
total_feminino = 0

for i in range(total_pessoas):
    print(f"Pessoa {i + 1}")
    
    while True:
        sexo = input("Informe o sexo (M/F): ").upper()
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

#Desafio: Criar um script 
# Python que analisa qualquer frase digitada pelo usuário e conta automaticamente 
# quantas vogais ela contém. O programa deve funcionar para letras maiúsculas e minúsculas.

vogais = "A", "E", "I", "O", "U"
frase = input("Informe uma frase: ").upper()
contador_vogais = 0
for i in frase:
    if i in vogais:
        contador_vogais+=1
        
print(f"A frase contém {contador_vogais} vogais.")
    

