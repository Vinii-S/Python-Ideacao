#2. Leia 5 números e imprima o menor

menor = int(input("Digite o 1 número: "))
for i in range(4):
   a = int(input(f"Digite o {i+2} número: "))
   if(a<menor):
      menor = a
 
print(f"Menor número digitado: {menor}")
