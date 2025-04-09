#14 Faça um algoritmo que leia 03 números e informe qual o maior deles


maior = 0
for num in range (3):
    num = int(input("Digite um número: "))
    if(num>maior):
        maior = num

print(f"O maior número digitado foi: {maior}")