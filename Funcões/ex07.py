import random

def jogo_craps():
    while True:
        input("Pressione Enter para girar os dados...")
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        total = dado1 + dado2
        print("Você obteve: ", total)

        if total == 7 or total == 11:
            print("Natural! Ganhou!")
            break
        elif total == 2 or total == 3 or total == 12:
            print("Craps! Perdeu!")
            break
        else:
            print("Sua pontuação é", total)
            while True:
                input("Pressione Enter para girar os dados novamente...")
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                novo_total = dado1 + dado2
                print("Você obteve: ", novo_total)
                if novo_total == total:
                    print("Ponto! Ganhou!")
                    return
                elif novo_total == 7:
                    print("Você tirou um 7. Perdeu!")
                    return
jogo_craps()
