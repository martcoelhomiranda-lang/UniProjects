# Construir um algoritmo que calcule a média aritmética de vários valores inteiros
# positivos, digitados pelo usuário. O final da leitura acontecerá quando for lido um
# valor negativo.

soma = 0
quantidade = 0
numero = int(input("Digite um número (negativo para encerrar): "))

while numero >= 0:
    soma += numero
    quantidade += 1
    numero = int(input("Digite um número (negativo para encerrar): "))

if quantidade > 0:
    print(f"Média: {soma / quantidade}")
else:
    print("Nenhum valor foi digitado.")
