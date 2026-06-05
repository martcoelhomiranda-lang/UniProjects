# 7.Escrever a função que recebe por parâmetro uma string e um caracter. e
# a função deve retornar os primeiros caracteres da string até encontrar o
# caracter passado por parâmetro

def encontrar_caractere(vetor):
    if len(vetor) != 0:
        resultado = ""
        i = 0
        while i < len(vetor[0]) and vetor[0][i] != vetor[1]:
            resultado += vetor[0][i]
            i += 1

        return resultado

vetor = ["arroz", "o"]
print(encontrar_caractere(vetor))


