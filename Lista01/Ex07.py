salário_atual = float(input("Digite seu salário atual: "))
tempo_serviço = float(input("Digite seu tempo na empresa em anos: "))

if tempo_serviço <= 1:
    percentual = 1.1
else:
    percentual = 1.2
salario_reajustado = salário_atual * percentual
print("Seu salário agora é:", salario_reajustado )
