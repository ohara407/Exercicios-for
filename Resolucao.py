"""
Resolução das questões incorretas do teste de Estruturas de Controle de Repetição em Python.
Você pode executar este arquivo para testar a saída real de cada questão!
"""

# Questão 4

print("Questão 4")
x = 20
while x > 0:
    x -= 6
    if x < 5:
        break
print(x)

# 1. x começa com 20.
# 2. 1 iteração: x vira 14 (20 - 6). 14 < 5 é falso.
# 3. 2ª iteração: x vira 8 (14 - 6). 8 < 5 é falso.
# 4. 3ª iteração: x vira 2 (8 - 6). Como 2 < 5 é verdadeiro, o break é acionado.
# 5. O print exibe o valor final de x: 2.



# Questão 5

print("Questão 5")
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Fim")

# EXPLICAÇÃO:
# 1. O loop imprime 0, 1 e 2.
# 2. Quando i vira 3, a condição 3<3 torna falsa.
# 3. Como o loop terminou normalmente sem break, o bloco else é executado e imprime Fim.



# Questão 6

print("Questão 6")
i = 0
while i < 5:
    if i == 2:
        break
    i += 1
else:
    print("Terminou")
print(i)

# EXPLICAÇÃO:
# 1. Quando i chega a 2, a condição do if é atingida e dispara o break.
# 2. Como o loop foi interrompido por um break, o bloco else é TOTALMENTE IGNORADO.
# 3. Executa apenas a instrução fora do laço: print, exibindo 2.



# Questão 9

print(" Questão 9")
for i in range(10, 0, -4):
    print(i)

# EXPLICAÇÃO:
# 1. range(10, 0, -4) inicia em 10, reduz de 4 em 4 e encerra antes de atingir 0.
# 2. 1ª iteração: i = 10
# 3. 2ª iteração: i = 6 (10 - 4)
# 4. 3ª iteração: i = 2 (6 - 4)
# 5. A próxima etapa seria -2, que ultrapassa o limite final (0), então o loop encerra.



# Questão 10

print("Questão 10")
palavra = "Python"
cont = 0
for letra in palavra:
    if letra in "aeiou":
        cont += 1
print(cont)

# 1. Verifica quais caracteres da string estão na sequência de vogais minúsculas "aeiou".
# 2. A palavra "Python" tem apenas uma vogal minúscula: 'o'.
# 3. O contador acumula apenas 1.



# Questão 11

print("Questão 11")
texto = "abc"
resultado = ""
for c in texto:
    resultado = c + resultado
print(resultado)

# 1. c = 'a': resultado = 'a' + ""   -> "a"
# 2. c = 'b': resultado = 'b' + "a"  -> "ba"
# 3. c = 'c': resultado = 'c' + "ba" -> "cba"
# A nova letra é concatenada ANTES da string acumulada, invertendo o texto.


# Questão 12

print("Questão 12")
numeros = [3, 8, 5, 10]
total = 0
for n in numeros:
    if n % 2 == 0:
        total += n
print(total)

# 1. Filtra e soma apenas os números pares (n % 2 == 0).
# 2. Pares da lista: 8 e 10.
# 3. Total: 8 + 10 = 18.



# Questão 13

print("Questão 13")
nomes = ["Ana", "Bia", "Caio", "Davi"]
for nome in nomes:
    if nome == "Caio":
        break
    print(nome)

# EXPLICAÇÃO:
# 1. Imprime "Ana".
# 2. Imprime "Bia".
# 3. Quando encontra "Caio", o 'break' é acionado ANTES de executar o print. O laço encerra.


# Questão 14

print("Questão 14")
numeros = [4, 9, 12, 7]
for n in numeros:
    if n > 10:
        print("Achou", n)
        break
else:
    print("Não achou")

# 1. 4 e 9 não são maiores que 10.
# 2. O número 12 atende à condição (12 > 10), imprime "Achou 12" e executa o 'break'.
# 3. O 'else' do laço só executaria se NENHUM número > 10 fosse encontrado.



# Questão 18 (Conceitual)

"""
Pergunta: Em Python, quando o bloco else de um for ou while é executado?

RESPOSTA CORRETA: 
Quando o laço termina normalmente, sem ser interrompido por um break.
"""