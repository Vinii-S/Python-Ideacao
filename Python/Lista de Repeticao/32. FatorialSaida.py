numero = int(input("Digite um número para descobrir o fatorial: "))
fatorial = 1
listaFatoriais = []
for num in range(numero):
    fatorial = fatorial * (numero - num)
    listaFatoriais.append(numero-num)
print(f"{numero}! = {' . '.join(str(x) for x in listaFatoriais)} = {fatorial}")