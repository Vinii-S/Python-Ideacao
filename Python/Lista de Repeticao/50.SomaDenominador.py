denominador = int(input("Digite o denominador: "))
soma = 0
termos = []

for n in range(1,denominador+1):
    termos.append(f"1/{n}")
    soma += (1/n)

expressao = " + ".join(termos)
print(f"H = {expressao}")
print(f"Resultado da soma de H: {soma:.2f}")