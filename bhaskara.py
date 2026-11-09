""""
def bhaskara(a,b,c):
    delta = (b ** 2) - 4*a*c
    if delta < 0:
        print("Não possui raizes reais")
    elif delta >= 0:
        x1 = (-b + delta ** 0.5 )/ (2 * a)
        x2 = (-b - delta ** 0.5)/ (2 * a)
        print(x1,x2)
bhaskara(1,-5,6)
"""
x= 0
try:
    print(x)
except:
    print("Algum erro ocorreu")
finally:
    print("O try e except foram finalizados")
    

