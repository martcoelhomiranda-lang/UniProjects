# Escrever uma função verificarEstacao(dia, mes), que
# retorna qual a estação do ano da data passada por
# parâmetro. Lembrando que a primavera começa no dia
# 23 de setembro, o verão em 21 de dezembro, o outono
# em 21 de março e o inverno em 21 de junho.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))

def verificarEstacao(dia , mes):

    estacao = " "

    if (mes >= 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
        estacao = "Outono"
    else:
        if (mes >= 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia < 23):
            estacao = "Inverno"
        else:
            if (mes >= 9 and dia >= 23) or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
                estacao = "Primavera"
            else:
                if (mes >= 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
                    estacao = "Verao"

    return estacao

print(f"A estacao é: {verificarEstacao(dia, mes)}")
