# 2.	Implemente uma função que retorne o
# maior elemento de um vetor de inteiros.

def retornar_maior_elemento(valores):
    if len(valores) != 0:
        maior = valores[0]
        for i in range(len(valores)):
            if valores[i] > maior:
                maior = valores[i]
        return maior

valores = [4, 6, 7, 8, 1, 2, 3, 9, 0]
print(retornar_maior_elemento(valores))