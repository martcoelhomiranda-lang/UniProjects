# 10.Escrever uma função que substitui por zero todos os números negativos
# do vetor passado por parâmetro.

def substituir_por_zero(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0

    return vetor

vetor = [-1,2,-3,4,-5,6,-7,8,-9,10]
print(substituir_por_zero(vetor))

