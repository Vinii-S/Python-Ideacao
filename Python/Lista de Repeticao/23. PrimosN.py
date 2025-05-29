numero = int(input("Digite um número e descubra todos os primos até ele: "))
primos = []
divisoes = 0
for n in range(2,numero + 1):
    primo = True
    for i in range(2,n):
        divisoes+=1
        if(n%i==0):
            primo = False
            break
    if(primo):
        primos.append(n)
    
print(f"Esses são todos os números primos até {numero} \n{primos}")
print(f"Numero total de divisões executadas: {divisoes}")