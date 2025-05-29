numerosAluno = []
alturasAlunos = []

for i in range (10):
    numeroAluno = int(input("Digite o número do aluno: "))
    alturaAluno = float(input("Digite a altura do aluno em m: "))
    numerosAluno.append(numeroAluno)
    alturasAlunos.append(alturaAluno)

maisAlto = alturasAlunos.index(max(alturasAlunos))
maisBaixo = alturasAlunos.index(min(alturasAlunos))

print(f"O aluno de número {numerosAluno[maisAlto]} é o aluno mais alto com {alturasAlunos[maisAlto]:.2f}")
print(f"O aluno de número {numerosAluno[maisBaixo]} é o aluno mais baixo com {alturasAlunos[maisBaixo]:.2f}")