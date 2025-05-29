preco = float(input("Informe o preço da unidade do pão em R$: "))

print("Panificadora Pão de Ontem - Tabela de Preços: ")

for i in range (1,51):
    print(f"{i} - R${preco * i :.2f}")
    