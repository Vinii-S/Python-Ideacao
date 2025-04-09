#15 Faça um algoritmo que leia 03 números e informe qual o menor deles

menor = int(input("Digite um número: "))
for num in range (2):
    num = int(input("Digite um número: "))
    if(num<menor):
        menor = num

print(f"O menor número digitado foi: {menor}")