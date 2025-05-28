numero = int(input("Digite um número para descobrir o fatorial: "))
fatorial = 1
for num in range(numero):
    fatorial = fatorial * (numero - num)
print(f"O fatorial de {numero} é {fatorial}")