gabarito = ["A","B","C","D","E","E","D","C","B","A"]

notas = []
while True:
    usarSistema = input("Algum aluno vai usar o sistema? Sim ou Não: ")
    if usarSistema.lower() == "não":
        break
    else:
        pontos = 0
        for i in range (0,10):
            resposta = input(f"Digite a sua resposta da Questão {i+1}: ")
            if(resposta.lower() == gabarito[i].lower()):
                pontos += 1
        notas.append(pontos)
        print(f"Sua nota foi {pontos}")

maiorNota = max(notas)
menorNota = min(notas)
qtdAlunos = len(notas)
mediaNotas = sum(notas) / qtdAlunos

print(f"A maior nota da prova foi {maiorNota}")
print(f"A menor nota da prova foi {menorNota}")
print(f"O numero de alunos que usaram o sistema foi {qtdAlunos}")
print(f"A média das notas da prova foi {mediaNotas}")
print(f"O gabarito da prova era: {gabarito}")
