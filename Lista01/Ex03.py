nota = int(input("Digite a nota do aluno: "))

if nota < 0:
    print("Nota Inválida")
else:
    if nota > 100:
        print("Nota Inválida")
    else:
        if nota >= 60:
            print("Aprovado")
        else:
            if nota < 60:
                print("Reprovado")
            else:
                if nota > 100:
                    print("Nota Inválida")
