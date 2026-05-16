# informar o numero do mes do ano e mostrar o nom e do mes por extenso.
# Caso o numero do mes nao exista, exibir a mensagem "mes invalido"

mes = int(input("Digite o mes atual: "))

if mes <= 0:
    print("Mes invalido")
else:
    if mes >= 13:
        print("Mes invalido")
    else:
        if mes == 1:
            print("Janeiro")
        else:
            if mes == 2:
                print("Fevereiro")
            else:
                if mes == 3:
                    print("Março")
                else:
                    if mes == 4:
                        print("Abril")
                    else:
                        if mes == 5:
                            print("Maio")
                        else:
                            if mes == 6:
                                print("Junho")
                            else:
                                if mes == 7:
                                    print("julho")
                                else:
                                    if mes == 8:
                                        print("Agosto")
                                    else:
                                        if mes == 9:
                                            print("Setembro")
                                        else:
                                            if mes == 10:
                                                print("Outubro")
                                            else:
                                                if mes == 11:
                                                    print("Novembro")
                                                else:
                                                    if mes == 12:
                                                        print("Dezembro")
