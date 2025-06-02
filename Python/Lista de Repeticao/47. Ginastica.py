notas = []
nomes = []
numJurados = 7
while True:
    nome = input("Informe o nome do atleta ou 'sair' para encerrar: ")
    nomes.append(nome)
    if (nome=="sair"):
        break
    for i in range (numJurados):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    maiorNota = max(notas)
    piorNota = min(notas)
    medianotas = (sum(notas) - maiorNota - piorNota) / (len(notas) - 2)
    print(f"Atleta: {nome}")
    for n in range (len(notas)):
        print(f"Nota: {notas[n]}")
    print("Resultado final: ")
    print(f"Atleta: {nome}\nMelhor Nota: {maiorNota}\nPior nota: {piorNota}\nMédia: {medianotas}")
    