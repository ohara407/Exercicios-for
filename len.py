"""""
letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]

print(f"tamanho da lista: {len(letra)}")
print(f"endereço da letra b: {letra.index('y')}")
"""""
"""""
letras = ["a", "b", "c", "d", "e", "f"]
var = input("informe uma letra:")
if var.lower() in letras:
    print(f"A letra {var.lower()} está na lista")
else:
    print(f"A letra {var.lower()} Não está na lista")
    """""
""""
nova = []
while True:
    num = int(input("Digite um numero inteiro(0 para sair): "))
    if num==0:
        break
    nova.append(num)
print(nova)
"""
""""
lista = []
while len(lista) < 5:
    num = int(input("Infome 5 numeros inteiros(0 para sair) "))
    if num == 0:
        break
    lista.append(num)
print(lista) 
"""
""""
lista = []
while len(lista) < 10:
    num = float(input("Infome 10 numeros reais(0 para sair) "))
    if num == 0:
        break
    lista.append(num)
    lista.reverse()
print(lista)
"""
"""
nota = []
soma = 0
while len(nota) < 4:
    valor_nota = float(input("Informe 4 notas do aluno (0 para sair): "))
    if valor_nota == 0:
        break
    nota.append(valor_nota)
    soma += valor_nota
    
media = soma / len(nota)
print(f"a soma da media é {media:.2f}")
"""
"""
one_tupla = (1,2,3,4)
tupla = one_tupla[2]
print(f"O segundo numero é: {tupla}")
"""
"""
one_tupla = (1,2,3,4)
second_tupla = ("A","B","C","D")
print({second_tupla[3]})
print({one_tupla[2]} )
"""
tupla_numero = (5,10,15,20)
lista_numero = list(tupla_numero)
lista_numero.append(25)
print(lista_numero)