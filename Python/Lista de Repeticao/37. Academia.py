alturas = []
pesos = []
codigos = []
mediaAltura = 0
mediaPeso = 0
while True:
    codigo = int(input("Informe seu codigo da academia: "))
    if(codigo==0):
        break
    altura = float(input("Digite a altura em cm: "))
    peso = float(input("Digite o peso em kg: "))
    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)
    
maisAlto = alturas.index(max(alturas))
maisBaixo = alturas.index(min(alturas))
maisGordo = pesos.index(max(pesos))
maisMagro = pesos.index(min(pesos))   
mediaAltura = sum(alturas) / len(alturas)
mediaPeso = sum(pesos) / len(pesos)

print(f"O código do aluno mais alto é {codigos[maisAlto]} e ele tem {alturas[maisAlto]:.2f}cm de altura")
print(f"O código do aluno mais baixo é {codigos[maisBaixo]} e ele tem {alturas[maisBaixo]:.2f}cm de altura")
print(f"O código do aluno mais gordo é {codigos[maisGordo]} e ele pesa {pesos[maisGordo]:.2f}kg")
print(f"O código do aluno mais magro é {codigos[maisMagro]} e ele pesa {pesos[maisMagro]:.2f}kg")
print(f"A media de alturas dos alunos é {mediaAltura}")
print(f"A media de pesos dos alunos é {mediaPeso}")