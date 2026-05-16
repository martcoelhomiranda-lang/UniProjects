# Faca um algoritmo que receba o valor do salario de uma pessoa e o valor
# de um financiamento pretendido. Caso o financiamento seja menor ou igual
# a 5 vezes o salario da pessoa, o algoritmo deverá escrever "Financiamento
# Concedido", senao, ele devera escrever "Fiananciamento Negado"

Salário_atual = float(input("Digite seu salario atual: "))
Financiamento = float(input("Digite o valor do financiamento: "))

Financiamento_possivel = Salário_atual * 5

if Financiamento > Financiamento_possivel:
    print("Financiamento Negado")
else:
    print("Financiamento Concedido")