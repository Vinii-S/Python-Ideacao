intervalo25 = []
intervalo50 = []
intervalo75 = []
intervalo100 = []
while True:
    numero = int(input("Digite um numero positivo para continuar e um negativo para parar: "))
    if(numero>=0 and numero<=25):
            intervalo25.append(numero)
    elif(numero>=26 and numero<=50):
        intervalo50.append(numero)
    elif(numero>=51 and numero<=75):
        intervalo75.append(numero)
    elif(numero>=76 and numero<=100):
        intervalo100.append(numero)
    elif(numero<0):
        break
print(f"Dentre os números que você digitou {len(intervalo25)} estão no intervalo [0-25], são eles: {intervalo25}")        
print(f"Dentre os números que você digitou {len(intervalo50)} estão no intervalo [26-50], são eles: {intervalo50}")        
print(f"Dentre os números que você digitou {len(intervalo75)} estão no intervalo [51-75], são eles: {intervalo75}")        
print(f"Dentre os números que você digitou {len(intervalo100)} estão no intervalo [76-100], são eles: {intervalo100}")        