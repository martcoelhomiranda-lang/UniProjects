# Faça uma função que recebe por parâmetro o raio de
# uma esfera e calcule o seu volume (v = (4 x pi x R^3)/3)

def calcular_volume(volume):
    return (( 4 * 3.14 * volume**3 ) / 3)

raio = int(input("Digite o valor do raio da esfera: "))
print(f"O volume da esfera é: {calcular_volume(raio):.2f}")