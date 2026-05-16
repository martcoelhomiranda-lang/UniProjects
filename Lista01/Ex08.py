Ano_atual = int(input("Digite o ano atual: "))
Ano_de_nascimento = int(input("Digite o ano de nascimento: "))
idade = Ano_atual - Ano_de_nascimento
print(f"Idade:{idade}")

if idade < 0:
    print("idade invalida")
else:
    if idade <= 3:
            print("Essa pessoa e um bebe")
    else:
        if idade <= 11:
            print("Essa pessoa e uma criança")
        else:
            if idade <= 17:
                print("Essa pessoa e um adolescente")
            else:
                if idade <= 64:
                    print("Essa pessoa e um adulto")
                else:
                    print("Essa pessoa e um idoso")
