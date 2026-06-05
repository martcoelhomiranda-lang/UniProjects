# 5.Escrever uma função que recebe por parâmetro um vetor de inteiros e
# retorna a soma de seus elementos

def somar_vetor(vetor):
    if len(vetor) != 0:
        soma = 0
        for i in range(len(vetor)):
            soma += vetor[i]
        return soma

vetor = [ 4, 5, 3, 9, 2, 2 ]
print(somar_vetor(vetor))