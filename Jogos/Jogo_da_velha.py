import random

def jogada_jogador():
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input("Digite a coluna (0, 1 ou 2): "))

    if not tabuleiro[linha][coluna]:
        tabuleiro[linha][coluna] = simbolo_jogador
        return linha, coluna
    else:
        print("Lugar já ocupado, tente novamente!")
        return jogada_jogador()

def jogada_maquina(rodada_maquina):
    rodada_maquina += 1

    if rodada_maquina <= 1:
        linha, coluna = randomizar_jogada()
    else:
        jogada = encontrar_jogada_vencedora(simbolo_maquina)
        if jogada:
            tabuleiro[jogada[0]][jogada[1]] = simbolo_maquina
            linha, coluna = jogada[0], jogada[1]
        else:
            jogada = encontrar_jogada_vencedora(simbolo_jogador)
            if jogada:
                tabuleiro[jogada[0]][jogada[1]] = simbolo_maquina
                linha, coluna = jogada[0], jogada[1]
            else:
                linha, coluna = randomizar_jogada()

    return linha, coluna, rodada_maquina

def randomizar_jogada():
    linha = random.randint(0, 2)
    coluna = random.randint(0, 2)

    if not tabuleiro[linha][coluna]:
        tabuleiro[linha][coluna] = simbolo_maquina
        return linha, coluna
    else:
        return randomizar_jogada()

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

    return None

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

# VARIAVEIS
vencedor = 0
rodada_maquina = 0
turno = random.randint(1, 2)

tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

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

# WHILE
while vencedor == 0:
    if turno == 1:
        print("Sua jogada:")
        linha, coluna = jogada_jogador()
        imprimir_tabuleiro()
        if verificar_possibilidade(linha, coluna, simbolo_jogador):
            vencedor = 1
            print("Você ganhou!")
        turno = 2
    else:
        print("Jogada da máquina:")
        linha, coluna, rodada_maquina = jogada_maquina(rodada_maquina)
        imprimir_tabuleiro()
        if verificar_possibilidade(linha, coluna, simbolo_maquina):
            vencedor = 2
            print("Máquina ganhou!")
        turno = 1

    if verificar_velha() and vencedor == 0:
        vencedor = 3
        print("Velha!")










