""""
def fahr_to_celsius(temp):
  

    Função que recebe como argumento uma temperatura em Fahrenheit e converte para celsius

    return ((temp - 32) * (5/9))
print(fahr_to_celsius(91.76))
print(fahr_to_celsius(101.3))
celsius =  fahr_to_celsius(70.76)
print(celsius)
"""

"""
def cumprimentar(nome):
    print("Olá", nome)

# Indentação a chamada do metodo não 
cumprimentar("ana")
"""

"""

def soma(n1,n2):
    soma = n1 + n2
    return soma
def subtracao(n1,n2):
    sub = n1 - n2
    return sub
def multiplicao(n1,n2):
    mult = n1 * n2
    return mult
def divisao(n1,n2):
    divisao = n1 / n2
    return divisao
def potenciacao(n1,n2):
    potenciacao = n1 ** n2
    return potenciacao 
def n1raizquadrada(n1):
    n1raizquadrada = n1 ** 0.5
def raiz(n):
    rz = n**0.5
    return rz


print("Bem vindo a calculadora")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

op = int(input("Selecione a operação: \n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão \n5-Potenciação \n6-Raiz Quadrada: "))
if op == 1:
    print(f"O valor da soma de {num1} e {num2} é {soma(num1, num2)}")
elif op == 2:
    print(f"O valor da subtracao de {num1} e {num2} é {subtracao(num1,num2)}")
elif op == 3:
    print(f"O valor da multiplicacao de {num1} e {num2} é {multiplicao(num1,num2)}")
elif op == 4 and num2 != 0:
    print(f"O valor da divisão de {num1} e {num2} é {divisao(num1, num2)}")
elif op == 4:
    print(f"O valor da potenciacao de {num1} e {num2} é {potenciacao(num1,num2)}")
elif op == 6 and num1 > 0 and num2 > 0:
    print(f'O valor da raiz quadrada de {num1} é {raiz(num1)} e a raiz quadrada de {num2} é {raiz(num2)}')
else:
    print("Comando Invalido")
    
    ##Digitar global() aparece todas as globais e locals() imprime todos os locals.
"""
"""
1. Crie uma função chamada apresentação que receba um nome, idade e curso como
parâmetro e imprima uma mensagem de apresentação para a sala.
2. Crie uma função chamada par_ou_impar que receba um número como parâmetro e
retorne "par" se ele for par e "ímpar" se for ímpar.
3. Crie uma função que converta uma temperatura de Fahrenheit para Celsius e para
Kelvin e print os dois.
"""

def apresentacao(nome, idade, curso):
    print(f"Olá, pessoal! Meu nome é {nome}, tenho {idade} anos e faço o curso de {curso}.")
apresentacao("Yago", 21, "Trilha Python/Back-end")

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def converte_temperatura(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273.15
    print(f"{fahrenheit}°F equivale a {celsius:.2f}°C e {kelvin:.2f}K")
    







print(par_ou_impar(4))  
print(par_ou_impar(7))  

converte_temperatura(77)



def contar_pares(n):
  contador = 0
  for i in range(1, n + 1):
    if i % 2 == 0:
      contador += 1
  return contador



def tamanho_palavra(texto):
  return len(texto)



def eh_primo(n):
  if n <= 1:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False  
  return True  

def preco_final(preco, porcentagem):
    porcentagem = porcentagem/100
    desc = preco * porcentagem
    preco_final = preco - desc
    return preco_final

def situacao(nota):
    if nota >= 7:
        print("APROVADO")
    elif nota <=6.9:
        print("RECUPERAÇÂO")
    else:
        print("REPROVADO")
        
def analisa_numero(numero):
    par = numero % 2 ==0
    dobro = numero * 2
    quadrado = numero ** 2
    if numero % 2 == 0:
        print(f"Seu numero é {par}, par")
    else:
        print("Seu numero é impar") 
    if numero > 0:
        print("Positivo")
    if numero < 0:
        print("Negativo")
    if numero == 0:
        print("seu numero é 0")
    if numero * 2:
        print("dobro", dobro)
    if numero ** 2:
        print(f"Quadrado {quadrado}")
        
def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        print("A equação não possui raízes reais")
    
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Raízes reais: x1 = {x1} e x2 = {x2}")

  


    
    



print("Teste de Contar Pares")
print(contar_pares(10)) 
print("\nTeste de Tamanho da Palavra")
print(tamanho_palavra("Python"))  

print("\nTeste de Número Primo")
print(eh_primo(1))  
print(eh_primo(2)) 
print(f"O preco final é, {preco_final(100, 30)}")

situacao(7)

analisa_numero(3)


print("\nTeste 1")
bhaskara(1, -5, 6) 
print("Teste 2")
bhaskara(1, 2, 5) 


