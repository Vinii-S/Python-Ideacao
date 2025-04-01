#7 Faça um algoritmo que leia as três notas do aluno Pedro e faça as seguintes operações
#a) Imprimir a Soma
#b) Imprimir a Média
#c) Imprimir se o aluno está aprovado, considere media 7

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

soma = n1 + n2 + n3
media = soma / 3
if media >=7:
    print(f" A média do aluno foi {media:.2f}, então ele foi Aprovado")
else:
    print(f" A média do aluno foi {media:.2f}, então ele foi Reprovado")