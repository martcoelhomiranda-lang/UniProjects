nome = input("Digite seu nome: ")
nota_P_1 = float(input("Digite a nota da primeira prova: "))
nota_P_2 = float(input("Digite a nota da segunda prova: "))
nota_T = float(input("Digite a nota do trabalho: "))
frequencia = float(input("Digite a quantidade de faltas: "))
media = ((nota_T + 2) + (nota_P_1 + 3) + (nota_P_2 + 5)) / 10

if frequencia > 15:
    print("Aluno reprovado")
else:
    if media >= 6:
        print("Aluno aprovado")
    else:
        print("Esta de final")
