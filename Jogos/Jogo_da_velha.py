import random

def jogada_jogador():
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        while linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Jogada inválida!")
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    if not tabuleiro[linha][coluna]:
        tabuleiro[linha][coluna] = simbolo_jogador
        return linha, coluna
    else:
        print("Lugar já ocupado, tente novamente!")
        return jogada_jogador()

def jogada_maquina():
    jogada = encontrar_jogada_vencedora(simbolo_maquina)
    if jogada:
        tabuleiro[jogada[0]][jogada[1]] = simbolo_maquina
        return jogada[0], jogada[1]

    jogada = encontrar_jogada_vencedora(simbolo_jogador)
    if jogada:
        tabuleiro[jogada[0]][jogada[1]] = simbolo_maquina
        return jogada[0], jogada[1]

    cantos = [[0,0], [2,2], [0,2], [2,0]]
    random.shuffle(cantos)
    for canto in cantos:
        if not tabuleiro[canto[0]][canto[1]]:
            tabuleiro[canto[0]][canto[1]] = simbolo_maquina
            return canto[0], canto[1]

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = simbolo_maquina
                return i, j

def encontrar_jogada_vencedora(jogador):
    for i in range(3):
        contador_jogador = 0
        contador_vazio = 0
        for j in range(3):
            if tabuleiro[i][j] == jogador:
                contador_jogador += 1
            if tabuleiro[i][j] == 0:
                contador_vazio += 1
        if contador_jogador == 2 and contador_vazio == 1:
            for j in range(3):
                if tabuleiro[i][j] == 0:
                    return i, j

        contador_jogador = 0
        contador_vazio = 0
        for j in range(3):
            if tabuleiro[j][i] == jogador:
                contador_jogador += 1
            if tabuleiro[j][i] == 0:
                contador_vazio += 1
        if contador_jogador == 2 and contador_vazio == 1:
            for j in range(3):
                if tabuleiro[j][i] == 0:
                    return j, i

    contador_jogador = 0
    contador_vazio = 0
    for i in range(3):
        if tabuleiro[i][i] == jogador:
            contador_jogador += 1
        if tabuleiro[i][i] == 0:
            contador_vazio += 1
    if contador_jogador == 2 and contador_vazio == 1:
        for i in range(3):
            if tabuleiro[i][i] == 0:
                return i, i

    contador_jogador = 0
    contador_vazio = 0
    for i in range(3):
        if tabuleiro[i][2-i] == jogador:
            contador_jogador += 1
        if tabuleiro[i][2-i] == 0:
            contador_vazio += 1
    if contador_jogador == 2 and contador_vazio == 1:
        for i in range(3):
            if tabuleiro[i][2-i] == 0:
                return i, 2-i

def verificar_possibilidade(linha, coluna, jogador):
    if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == jogador:
        return True
    if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
        return True
    if linha == coluna:
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
            return True
    if linha + coluna == 2:
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
            return True
    return False

def verificar_velha():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return False
    return True

def imprimir_tabuleiro():
    for i in range(3):
        for j in range(3):
            print(simbolos[tabuleiro[i][j]], end=" ")
        print()

def resetar_tabuleiro():
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = 0

placar_vitoria_j = 0
placar_vitoria_m = 0
placar_velha = 0
jogar_de_novo = True

tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

while jogar_de_novo == True :
    vencedor = 0
    turno = random.randint(1,2)
    resetar_tabuleiro()

    if turno == 1:
        print("Você começa! Você é o X")
        simbolo_jogador = 1
        simbolo_maquina = 2
        simbolos = {0: ".", 1: "X", 2: "O"}
    else:
        print("Máquina começa! Você é o O")
        simbolo_jogador = 2
        simbolo_maquina = 1
        simbolos = {0: ".", 1: "X", 2: "O"}

    imprimir_tabuleiro()

    while vencedor == 0:
        if turno == 1:
            linha, coluna = jogada_jogador()
            print("Sua jogada:")
            imprimir_tabuleiro()
            if verificar_possibilidade(linha, coluna, simbolo_jogador):
                vencedor = 1
                print("Você ganhou!")
                placar_vitoria_j += 1
            turno = 2
        else:
            print("Jogada da máquina:")
            linha, coluna = jogada_maquina()
            imprimir_tabuleiro()
            if verificar_possibilidade(linha, coluna, simbolo_maquina):
                vencedor = 2
                print("Máquina ganhou!")
                placar_vitoria_m += 1
            turno = 1

        if verificar_velha() and vencedor == 0:
            vencedor = 3
            print("Velha!")
            placar_velha += 1
    print()
    print(f"Placar - Você: {placar_vitoria_j} | Máquina: {placar_vitoria_m} | Velhas: {placar_velha}")
    resposta = input("Quer jogar de novo? (s/n): ")
    if resposta != "s":
        jogar_de_novo = False