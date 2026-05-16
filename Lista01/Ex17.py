# Escreva um programa que receba dois números reais e um código de seleção do usuário. Se o código digitado for 1,
# faça o programa adicionar os dois números previamente digitados e mostrar o resultado; se o código de seleção for 2,
# os números devem ser multiplicados; se o código de seleção for 3, o primeiro número deve ser dividido pelo segundo.
# Se nenhuma das opções acima for escolhida, mostrar "Código inválido".

n_1 = int(input("Digite o primeiro numero: "))
n_2 = int(input("Digite o segundo numero: "))
cod = int(input("Digite o codigo: "))

if cod < 1 or cod > 3:
        print("Codigo invalido")
else:
    if cod == 1:
        cod_1 = cod + n_1 + n_2
        print(cod_1)
    else:
        if cod == 2:
            cod_2 = n_2 * n_1
            print(cod_2)
        else:
            if cod == 3:
                cod_3 = n_1 / n_2
                print(cod_3)
