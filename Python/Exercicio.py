#1. Leia 3 números e imprima somente o maior
""""
maior = 0
for i in range(3):
   a = int(input(f"Digite o {i+1} número: "))
   if(a>maior):
      maior = a
    
print(f"Maior número impresso foi {maior}")
"""

#2. Leia 5 números e imprima o menor
"""
menor = int(input("Digite o 1 número: "))
for i in range(4):
   a = int(input(f"Digite o {i+2} número: "))
   if(a<menor):
      menor = a
 
print(f"Menor número digitado: {menor}")
"""

#3. Leia 3 números e imprima em ordem crescente

num1 = int(input("Digite o 1 valor: "))
num2 = int(input("Digite o 2 valor: "))
num3 = int(input("Digite o 3 valor: "))

numeros = [num1,num2,num3]
numeros.sort()

print("Imprimindo em ordem crescente", numeros)

#4. Imprima se o aluno é maior de idade
"""
idade = int(input("Digite sua idade: "))
if(idade>=18):
   print("Você é maior de idade.")
else:
   print("Você é de menor.")
"""
#5. Leia 3 números e imprima de forma decrescente
num1 = int(input("Digite o 1 valor: "))
num2 = int(input("Digite o 2 valor: "))
num3 = int(input("Digite o 3 valor: "))

if(num1 >= num2) and (num2>=num3):
    print(num1,num2,num3)
elif(num1>=num3) and (num3>=num2):
    print(num1,num3,num2)
elif(num2>=num1) and (num1>=num3):
    print(num2,num1,num3)
elif(num2>=num3) and (num3>=num1):
    print(num2,num3,num1)
elif(num3>=num1) and (num1>=num2):
    print(num3,num1,num2)
else:
    print(num3,num2,num1)


#6. Dado um valor X perguntar se esse é maior ou menor que 20 e imprima a resposta

x = int(input("Digite um valor: "))
resp = input("Esse valor é maior que vinte? ")
print(resp)
if(x>20):
   print(f"{x} é menor que 20.")
else:
   print(f"{x} é menor que 20")
