# Em uma eleição presidencial existem quatro candidatos. Os votos são informados
# através de códigos. Os dados utilizados para a contagem dos votos obedecem à
# seguinte codificação:
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 6 = voto em branco.
# Elabore um algoritmo que leia o código do candidato em um voto. Calcule e
# escreva as seguintes informações:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco.
# Como finalizador do conjunto de votos, utilize o valor 0.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0
voto = 1
while True:
    voto = int(input("Digite o seu voto (1-4 para candidatos, 5 para nulo , 6 para branco e 0 para encerrar o processo): "))
    if voto < 0 or voto > 6:
        print("Voto invalido")
    else:
        if voto == 0:
            break
        else:
            if voto == 1:
                candidato1 += 1
            else:
                if voto == 2:
                    candidato2 += 1
                else:
                    if voto == 3:
                        candidato3 += 1
                    else:
                        if voto == 4:
                            candidato4 += 1
                        else:
                            if voto == 5:
                                nulos += 1
                            else:
                                brancos += 1
print(f"Votos no cantidato 1: {candidato1}")
print(f"Votos no cantidato 2: {candidato2}")
print(f"Votos no cantidato 3: {candidato3}")
print(f"Votos no cantidato 4: {candidato4}")
print(f"Votos nulos: {nulos}")
print(f"Votos em branco: {brancos}")