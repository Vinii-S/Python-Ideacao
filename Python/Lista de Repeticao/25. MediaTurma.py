qtd = int(input("Informe a quantidade de pessoas na turma: "))
soma = 0
for i in range(qtd):
    idade = int(input(f"Informe a {i+1}ª idade: "))
    soma += idade
media = soma / qtd
if(media>=0 and media<=25):
    print(f"A media das idades foi: {media:.2f}, portanto, a turma é Jovem.")
elif (media>=26 and media <=60):
    print(f"A media das idades foi: {media:.2f}, portanto, a turma é Adulta.")
elif(media>60):
    print(f"A media das idades foi: {media:.2f}, portanto, a turma é Idosa.")
    