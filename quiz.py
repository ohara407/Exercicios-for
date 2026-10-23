pontos = 0
vidas = 3
while vidas > 0:
    quiz = input("Participe do quiz true ou false para as respostas, atente-se você so tem 3 vidas digite -1 para começar, 2- para sair")
    if quiz == "1" or quiz == "começar":
        p_q1 = input("É Verdade que você é gay true or false")
        if p_q1 == "true":
            print(f"Já suspeitava {pontos} ")
            pontos +=1
        else:
            vidas -= 1
            print(f"Resposta incorreta. Você perdeu 1 vida! Vidas restantes: {vidas}")