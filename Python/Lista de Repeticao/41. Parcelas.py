divida = float(input("Digite o valor da sua dívida em R$: "))

print("QUANTIDADE DE PARCELAS E JUROS:")
print("1 parcela - 0% de juros")
print("3 parcela - 10% de juros")
print("6 parcela - 15% de juros")
print("9 parcela - 20% de juros")
print("12 parcela - 25% de juros")

parcelas = int(input("Digite a quantidade de parcelas que deseja: "))
taxaJuros = 0
valorJuros = 0
valorParcela = 0

if parcelas == 1:
    taxaJuros = 0
    valorJuros = 0 
    valorParcela = divida
elif(parcelas == 3):
    taxaJuros = 0.1
    valorJuros = divida * taxaJuros
    valorParcela = (divida + valorJuros) / parcelas
elif(parcelas == 6):
    taxaJuros = 0.15
    valorJuros = divida * taxaJuros
    valorParcela = (divida + valorJuros) / parcelas
elif(parcelas==9):
    taxaJuros = 0.2
    valorJuros = divida * taxaJuros
    valorParcela = (divida + valorJuros) / parcelas
elif(parcelas==12):
    taxaJuros = 0.25
    valorJuros = divida * taxaJuros
    valorParcela = (divida + valorJuros) / parcelas

print("Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela")
print(f"{divida} - {valorJuros:.2f} - {parcelas} - {valorParcela:.2f}")