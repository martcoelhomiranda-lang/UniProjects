# 6.Escrever a função que recebe por parâmetro uma string e um número. A
# função deve retornar os primeiros caracteres da string de acordo com o
# número passado por parâmetro

def retornar_caractere(vetor):
    if len(vetor) != 0:
        resultado = ""
        for i in range(vetor[1]):
            resultado += (str(vetor[0][i]))

    return resultado

vetor = ["carros", 3]
print(retornar_caractere(vetor))