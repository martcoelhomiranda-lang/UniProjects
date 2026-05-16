#Pedra Papel e Tesoura
quantidade = int(input("Quantas vezes voce quer jogar?: "))
vitorias_humano = 0
vitorias_cpu = 0
empates = 0


for i in range(quantidade):

    from random import*
    cpu = randint(0,2)
    jogada = int(input("Digite sua jogada; 0 = PEDRA, 1 = PAPEL, 2 = TESOURA: "))

    if jogada < 0 or jogada > 2:
        print("Jogada invalida")
    else:
        print(f"Voce jogou {jogada} e o computador jogou {cpu} ")
        if jogada == cpu:
            print("Empate")
            empates = empates + 1
        else:
            if (jogada == 0 and cpu == 2) or (jogada == 2 and cpu == 1) or (jogada == 1 and cpu == 0):
                print("Jogador venceu!")
                vitorias_humano = vitorias_humano + 1
            else:
                print("Computador venceu!")
                vitorias_cpu = vitorias_cpu + 1
print("Vitorias do humano: ", vitorias_humano)
print("Vitorias da cpu: ", vitorias_cpu)

if empates > 0:
    print("Numero de empates: ", empates)
