qtdCds = int(input("Informe a quantidade de CDs: "))
soma = 0
for i in range(qtdCds):
    preco = float(input(f"Informe o preco do {i+1}º CD em R$: "))
    soma+=preco
media = soma / qtdCds
print(f"Você gastou um total de R$ {soma} com CDs, e cada CD custou em média R$ {media}")
    