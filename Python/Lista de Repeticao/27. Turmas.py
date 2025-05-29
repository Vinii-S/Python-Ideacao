qtdTurmas = int(input("Digite a quantidade de turmas: "))
totalAlunos = 0

for i in range(qtdTurmas):
    while True:
        alunos = int(input(f"Digite o número de alunos da turma {i+1}: "))
        if alunos <= 40:
            totalAlunos += alunos
            break
        else:
            print("Uma turma não pode ter mais de 40 alunos. Digite novamente.")

media = totalAlunos / qtdTurmas
print(f"\nA média de alunos por turma é: {media:.2f}")
