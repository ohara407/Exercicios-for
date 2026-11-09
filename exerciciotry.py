"""
try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")
except:
    print("Erro! Você digitou letras.")
print("O programa continua vivo... ")
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