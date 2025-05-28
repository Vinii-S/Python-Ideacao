lista = []

quantidade = int(input("Digite a quantidade de numeros que deseja inserir: "))

for i in range(quantidade):
    while len(lista)<quantidade:
        numero = int(input("Digite um número: "))
        lista.append(numero)

maior = lista[0]
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"O maior número da lista {lista} é {maior}, o menor é {menor} e a soma de todos os números é {sum(lista)}")
