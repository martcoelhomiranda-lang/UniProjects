# Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo correspondente.
# Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido. Utilize a tabela abaixo:
#
#  Código               Cargo
#   101                Vendedor
#   102                Atendente
#   103                Auxiliar
#   104                Assistente
#   105                Coordenador de Grupo
#   106                Gerente

cod = int(input("Digite o seu codigo: "))

if cod < 101 or cod > 106:
        print("Codigo invalido")
else:
    if cod == 101:
        print("Cargo: Vendedor")
    else:
        if cod == 102:
            print("Cargo: Atendente")
        else:
            if cod == 103:
                print("Cargo: Auxiliar")
            else:
                if cod == 104:
                    print("Cargo: Assistente")
                else:
                    if cod == 105:
                        print("Cargo: Cordenador de Grupo")
                    else:
                        if cod == 106:
                            print("Cargo: Gerente")
