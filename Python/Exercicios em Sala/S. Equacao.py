#19 Faça um algoritmo que leia 3 valores e aplique uma equacao do segundo grau
import cmath
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))

equacao1 = ((valorB*-1) + cmath.sqrt(valorB**2 - 4 * valorA * valorC)) / (2 * valorA)
equacao2 = ((valorB*-1) - cmath.sqrt(valorB**2 - 4 * valorA * valorC)) / (2 * valorA)

print(f"Se aplicarmos os valores informados em uma Equação do Segundo Grau teremos os seguintes resultados: \nX1: {equacao1:.2f} e X2: {equacao2:.2f}")