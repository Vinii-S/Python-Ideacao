#1. Leia 3 números e imprima somente o maior

maior = 0
for i in range(3):
   a = int(input(f"Digite o {i+1} número: "))
   if(a>maior):
      maior = a
    
print(f"Maior número impresso foi {maior}")