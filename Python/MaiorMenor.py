notas = [4,3,7,9,10,8,6,2,1,5]
maior = 0
menor = 10

for nota in notas:
    if(nota > maior):
        maior = nota
    elif (nota < menor):
        menor = nota

print("Maior nota", maior)
print("Menor nota", menor)

a = int (input("Digite o valor de A: "))
b = int (input("Digite o valor de B: "))

if(a > b):
    print(a)
else:
    print(b)
#if(notas.index)