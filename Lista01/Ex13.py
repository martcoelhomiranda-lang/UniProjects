ano = int(input("Qual o ano do carro? "))
peso = int(input("Qual o peso do carro? "))

if ano <= 1970:
    if peso < 1200:
        classe = 1
        taxa = 16,50 
    else:
        if peso <= 1200:
            classe= 2 
            taxa = 25,50
        else:
            classe =  3 
            taxa = 46,50
else:
    if ano <= 1979:
        if peso < 1200:
            classe = 4
            taxa = 27,00
        else:
            if peso <= 1200:
                classe = 5 
                taxa = 30,50 
            else:
                classe = 6
                taxa = 52,50 
    else:
        if ano >= 1980:
            if peso < 1600:
                classe = 7
                taxa = 19,50 
            else:
                classe = 8
                taxa = 55,50

