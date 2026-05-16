# Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos,
# calcule e imprima: a média dos números caso a soma deles for menor que 8,
# seu produto caso a soma seja igual a 8 ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.

n_1 = int(input("Digite o primeiro valor inteiro: "))
n_2 = int(input("Digite o segundo valor inteiro: "))

if n_1 < 1:
    print("Numero invalido")
else:
    if n_1 > 10:
        print("Numero valido")
    else:
        if n_2 < 1:
            print("Numero invalido")
        else:
            if n_2 > 10:
                print("Numero valido")
            else:
                if n_1 + n_2 < 8:
                    media = (n_1 + n_2) / 2
                    print(media)
                else:
                    if n_1 + n_2 == 8:
                        produto = n_1 * n_2
                        print(produto)
                    else:
                        if n_1 + n_2 > 8:
                            if n_1 > n_2:
                                div_1 = n_1 / n_2
                                print(div_1)
                            else:
                                div_2 = n_2 / n_1
                                print(div_2)
