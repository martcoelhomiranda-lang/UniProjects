# 9.Implemente uma função que retorne a média dos valores armazenados
# em um vetor de inteiros.

def media(vetor):
    if len(vetor) != 0:
        soma = 0
        for i in range(len(vetor)):
            soma += vetor[i]

    return soma/len(vetor)

vetor = [10,20]
print(media(vetor))
