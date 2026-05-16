# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
# sobre o salário e número de filhos. A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de um salário negativo.

habitantes = int(input("Digite a populaçao: "))
filhos = 0
salario = 0
percentual = 0
if habitantes < 0:
    print("Quantidade invalida")
else:
    if filhos < 0:
        print("Quantidade invalida")
    else:
        if salario < 0:
            print("Quantidade invalida")
            for i in range(habitantes):
                salario = int(input("Digite seu salario: "))
                filhos = int(input("Digite o numero de filhos: "))
        media_salario = salario / habitantes
        media_filhos = filhos / habitantes
        if salario <= 1000:
            percentual += 1
        print("A media salarial é:", media_salario)
        print("A media de filhos é:", media_filhos)
        print("Percentual de pessoas com salario ate 1000:", percentual / 100)