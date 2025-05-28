listaPares = []
listaImpares = []
for num in range(10):
    numero = int(input("Digite um número: "))
    if(numero%2==0):
        listaPares.append(numero)
    else:
        listaImpares.append(numero)
    
print(f"Dentre os 10 números que você digitou {len(listaPares)} deles são pares, e eles são: {listaPares}")
print(f"Dentre os 10 números que você digitou {len(listaImpares)} deles são ímpares e eles são: {listaImpares}")