numero = int(input("Digite um número e descubra todos os primos até ele: "))
primo = True
primos = []
for i in range(2,numero):
    if(numero%i==0):
        primo = False
    if(primo):
        primos.append(i)
    
print(f"Esses são todos os números primos até {numero} \n{primos}")
    