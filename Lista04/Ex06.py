# Escrever uma função calcularQuociente(dividendo,
# divisor), que retorna a divisão inteira (sem casas
# decimais) de dividendo por divisor e outra função
# calcularResto(dividendo, divisor) que retorna o
# resto.

dividendo = int(input("Digite o valor do dividendo : "))
divisor = int(input("Digite o valor do divisor : "))

def calcularQuociente(dividendo, divisor):
    resultado = dividendo // divisor
    return resultado

def calcularResto(dividendo, divisor):
    if divisor != 0
        resto = dividendo % divisor
        return resto

print(f"A divisao é: {calcularQuociente(dividendo, divisor):.2f}")
print(f"O resto da divisao é: {calcularResto(dividendo, divisor)}")
