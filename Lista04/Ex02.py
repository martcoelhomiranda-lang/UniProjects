# Faça uma função que recebe a média final de um aluno
# por parâmetro e retorna o seu conceito, conforme a
# tabela abaixo:

def parametro(media):
    conceito = " "
    if  media >= 90 and media <= 100:
        conceito = "a"
    else:
        if media >= 70 and media < 90:
            conceito = "b"
        else:
            if media >= 50 and media < 70:
                conceito = "c"
            else:
                conceito = "d"
    return conceito
media = int(input("Digite a sua média final: "))
print(f"O seu conceito é: {parametro(media)}")