maior = 0
for num in range (5):
    num = int(input("Digite um número: "))
    if(num>maior):
        maior = num

print(f"O maior número digitado foi: {maior}")