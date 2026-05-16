# Escrever um algoritmo que leia um número n que indica quantos valores devem ser
# lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.

n = int(input("Digite a quantidade de valores: "))
if n <= 0:
    print("Quantidade invalida")
else:
    for i in range(n):
        numero = int(input("Digite um numero: "))
        if numero <= 0:
            print("Numero invalido")
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"{numero}! = {fatorial}")
