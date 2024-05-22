def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("---+---+---")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def posicao_livre(tabuleiro, posicao):
    mapeamento = {
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (0, 0), 8: (0, 1), 9: (0, 2)
    }
    linha, coluna = mapeamento[posicao]
    return tabuleiro[linha][coluna] == " "

def jogada(tabuleiro, posicao, jogador):
    mapeamento = {
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (0, 0), 8: (0, 1), 9: (0, 2)
    }
    linha, coluna = mapeamento[posicao]
    tabuleiro[linha][coluna] = jogador

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        imprimir_tabuleiro(tabuleiro)
        
        posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): "))
        
        if posicao < 1 or posicao > 9:
            print("Posição inválida! Escolha um número entre 1 e 9.")
            continue
        if not posicao_livre(tabuleiro, posicao):
            print("Posição já ocupada! Escolha outra posição.")

        jogada(tabuleiro, posicao, jogador_atual)
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

jogo_da_velha()