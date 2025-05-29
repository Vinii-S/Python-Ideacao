print("Digite as temperaturas (Digite 'sair' para encerrar)")
temperaturas = []

while True:
    temperatura = input("Temperatura: ")
    if(temperatura.lower() == 'sair'):
        break
    temp = float(temperatura)
    temperaturas.append(temp)
    
menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"A menor temperatura foi: {menor}ºC")
print(f"A maior temperatura foi: {maior}ºC")
print(f"A media das temperatura foi: {media}ºC")