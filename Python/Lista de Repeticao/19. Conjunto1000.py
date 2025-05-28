lista = []

quantidade = int(input("Quantos números você deseja inserir? "))

for i in range(quantidade):
    while True:
        numero = int(input("Digite um número entre 0 e 1000: "))
        if 0 <= numero <= 1000:
            lista.append(numero)
            break
        else:
            print("Número inválido! Tente novamente.")

maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"\nLista digitada: {lista}")
print(f"O maior número é {maior}, o menor é {menor}, e a soma é {sum(lista)}")
