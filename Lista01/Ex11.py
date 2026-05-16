# Escreva um programa para calcular e mostrar o salario semanam de uma
# pessoa, determinado pelas condiçoes que seguem. Se o numero de hroas
# trabalhadas for inferior ou igual a 40, a pessoa recebe R$15,00 por hora,
# senao a pessoa recebe R$600,00 mais R$21,00 para cada hora trabalhado
# acima de 40 hora. o programa deve pedir o numero de horas trabalhadas
# como entrada e deve dar o salario como saida

horas = int(input("Digite sua quantidade de horas trabalhadas: "))

if horas < 1:
    print("Horas invalidas")
else:
    if horas <= 40:
        valor = horas * 15
        print(f"Seu salario é R${valor}")
    else:
        valor_2 = horas * 21 + 600
        print(f"Seu salario é R${valor_2}")
