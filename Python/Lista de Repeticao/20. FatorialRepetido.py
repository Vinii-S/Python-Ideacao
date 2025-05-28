while True:
    numero = int(input("Digite um número inteiro positivo menor que 16 para descobrir o fatorial (Se deseja parar digite -1): "))
    if numero == -1:
        break
    if(numero>16) or (numero<0):
        print("Número inválido, tente novamente")
        continue
    fatorial = 1
    for num in range(numero):
        fatorial = fatorial * (numero - num)
    print(f"O fatorial de {numero} é {fatorial}")