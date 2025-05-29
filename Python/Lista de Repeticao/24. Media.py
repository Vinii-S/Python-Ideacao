tamanho = int(input("Informe a quantidade de notas: "))
soma = 0
for i in range(tamanho):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    soma += nota
media = soma / tamanho
print(f"A media das notas foi: {media:.2f}")