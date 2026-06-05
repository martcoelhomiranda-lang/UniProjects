# 1.	Escrever uma função que receba um vetor com
# 10 valores e retorne quantos destes valores são
# negativos.

def contar_negativos(valores):
    quantidade = 0
    for i in range(len(valores)):
        if valores[i] < 0:
            quantidade += 1
    return quantidade

valores = []
for i in range(10):
    valor = int(input('Digite um valor: '))
    valores.append(valor)
print(contar_negativos(valores))