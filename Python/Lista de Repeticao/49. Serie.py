n = int(input("Digite o numerador: "))
m = int(input("Digite o denominador: "))
numerador = 1
denominador = 1
soma = 0
termos = []

while numerador <= n and denominador <= m:
    termos.append(f"{numerador}/{denominador}")
    soma += (numerador/denominador)
    numerador += 1
    denominador += 2

expressao = " + ".join(termos)
print(f"S = {expressao}")
print(f"Resultado da soma: {soma:.2f}")
