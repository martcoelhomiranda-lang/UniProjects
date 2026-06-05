# 4. Implemente uma função que ordene um vetor de inteiros de tamanho 10


def ordenar_vetor(vetor):
    if len(vetor) != 0:
        for j in range(len(vetor)):
            for i in range(1, len(vetor)):
                if vetor[i-1] > vetor[i]:
                    troca = vetor[i]
                    vetor[i] = vetor[i-1]
                    vetor[i-1] = troca

        return vetor

vetor = [ 4, 5, 3, 9, 1, 7, 18, 11, 10, 8 ]
print(ordenar_vetor(vetor))
