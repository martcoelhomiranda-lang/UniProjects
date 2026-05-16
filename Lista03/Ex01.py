# Faça um algoritmo que lê um valor N inteiro e
# positivo e que calcula e escreve o fatorial de N (N!).

numero = int(input("Digite um numero: "))
if numero <= 0:
    print("Numero invalido")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print(f"{numero}! = {fatorial}")