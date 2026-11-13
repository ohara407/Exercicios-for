"""
try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")
except:
    print("Erro! Você digitou letras.")
print("O programa continua vivo... ")
"""
"""
try:
    a = int(input('diga me um numero: '))
    b = int(input('diga me outro numero: '))
    print('a/b = ', a/b)
    print("a+b = ", a + b)
except ValueError:
    print('Não podemos converter para um número')
except ZeroDivisionError:
    print('Não Podemos dividir por zero')
except:
    print('algo de muito errado aconteceu')
"""
"""
def dividir_seguro(a,b):
    return a / b
try:
    n1 = float(input("Digite o primeiro numero "))
    n2 = float(input("Digite o segundo numero "))
    divisao = dividir_seguro(n1,n2)
except ZeroDivisionError:
    print("Não Pode ser por 0")
finally:
    print("Operação encerrada")
"""
"""
def divisao_segura(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Não Pode dividir por zero burrão !")
    else:
        print(f"O resultado da divisão é: {resultado}")
    finally:
        print("Operação finalizada !")
        
################################################

while True:
    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite outro valor: "))
    divisao_segura(num1,num2)
    continuar = input("Deseja continuar? S ou N ")
    if continuar == "N":
        print("Finalizando o programa")
"""

dicionario = {
    "produto": "maca",
    "valor": 3.50,  
} 
try:
    consulta = dicionario["valor"]
except KeyError:
    print("Erro")
    
finally:
    print("Operação encerrada")