#usar o operador in e o comando len(diz quantas letras tem naquela variavel)
acertos = 0
vidas = 7
letras_jogadas = ""

palavra = str(input("Digite uma palavra: ")).lower()
tamanho = (len(palavra))

while vidas != 0 and acertos != tamanho:
    exibicao = ""
    for letras in palavra:
        if letras in letras_jogadas:
            exibicao += letras
        else:
            exibicao += ""

    print(f"{exibicao} " )
    print(f"Letras jogadas: {letras_jogadas}")
    print(f"Você tem: {vidas} vidas!")

    letra = str(input("Digite uma letra: ")).lower()
    quantidade_let = len(letra)
    if quantidade_let != 1:
        print("Só pode jogar uma letra por vez!")
    else:
        if letra in letras_jogadas:
            print("Você já jogou essa letra!")
        else:
            if letra in palavra:
                print("Acertou!")
                acertos += palavra.count(letra)
            else:
                print("Errou!")
                vidas += -1
            letras_jogadas += letra + "-"

print(f"A palavra é {palavra}")
if acertos == tamanho:
    print("Você ganhou!")
else:
    print("Você perdeu!")