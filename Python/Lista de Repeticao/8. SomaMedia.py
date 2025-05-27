soma = 0
for num in range (5):
    num = int(input("Digite um número: "))
    soma+=num

media = soma / 5
print(f"A soma dos numeros digitados foi {soma} e a media foi {media:.2f}")