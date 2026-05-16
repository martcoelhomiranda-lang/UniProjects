# Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o
# código e o preço de custo de cada produto e calcule o preço novo. Calcule também,
# a média dos preços com e sem aumento. Mostre o código e o preço novo de cada
# produto e, no final, as médias. A entrada de dados deve terminar quando for lido
# um código de produto negativo.

codigo = int(input("Qual o codigo do produto?(negativo para encerrar) : "))
produtos = 0
soma_novo_preco = 0
soma_preco = 0
while codigo >= 0:
    produtos += 1
    preco = float(input("Qual o preço do produto?: "))
    novo_preco = preco * 1.2
    soma_novo_preco += novo_preco
    soma_preco += preco
    print(f"O novo valor do produto {codigo} é {novo_preco}")
    codigo = int(input("Qual o codigo do produto?(negativo para encerrar) : "))

print(f"A media do preço antigo é {soma_preco/produtos}")
print(f"A media do preço novo é {soma_novo_preco/produtos}")


