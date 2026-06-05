# 3.	Implemente uma função que retorne o
# menor elemento de um vetor de inteiros.

def retornar_menor_elemento(valores):
    if len(valores) != 0:
        menor = valores[0]
        for i in range(len(valores)):
            if valores[i] < menor:
                menor = valores[i]
        return menor

valores = [4, 6, 7, 8, 1, 2, 3, 9, 0]
print(retornar_menor_elemento(valores))
