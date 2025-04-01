#3. Leia 3 números e imprima em ordem crescente

num1 = int(input("Digite o 1 valor: "))
num2 = int(input("Digite o 2 valor: "))
num3 = int(input("Digite o 3 valor: "))

numeros = [num1,num2,num3]
numeros.sort()

print("Imprimindo em ordem crescente", numeros)
