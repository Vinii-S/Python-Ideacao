saltos = []
nomes = []
numSaltos = 5
while True:
    nome = input("Informe o nome do atleta ou 'sair' para encerrar: ")
    nomes.append(nome)
    if (nome=="sair"):
        break
    for i in range (numSaltos):
        salto = float(input(f"Digite a distância do {i+1}º salto em m: "))
        saltos.append(salto)
    maiorSalto = max(saltos)
    piorSalto = min(saltos)
    mediaSaltos = (sum(saltos) - maiorSalto - piorSalto) / (len(saltos) - 2)
    print(f"Atleta: {nome}")
    print(f"Primeiro Salto: {saltos[0]}")
    print(f"Segundo Salto: {saltos[1]}")
    print(f"Terceiro Salto: {saltos[2]}")
    print(f"Quarto Salto: {saltos[3]}")
    print(f"Quinto Salto: {saltos[4]}")
    print(f"Melhor Salto: {max(saltos)}")
    print(f"Pior Salto: {min(saltos)}")
    print(f"Media dos demais saltos: {mediaSaltos:.2f}")
    print("Resultado final: ")
    print(f"{nome}: {mediaSaltos:.2f}")
    