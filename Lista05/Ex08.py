# 8.Implemente uma função que, dado um valor, retorne se esse valor
# pertence ou não a um vetor de inteiros.

valor = int(input("Digite um valor: "))

def verficar(vetor):
    if len(vetor) != 0:
        for i in range(len(vetor)):
            if valor == vetor[i]:
                return True
        return False

vetor = [1, 2, 3, 4, 5]
print(verficar(vetor))

