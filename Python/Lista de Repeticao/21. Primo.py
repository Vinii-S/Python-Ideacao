numero = int(input("Digite um número e descubra se ele é primo: "))
primo = True
for i in range(2,numero):
    if(numero%i==0):
        primo = False
        break
    
if primo:
    print(f"O  numero {numero} é primo")
else:
    print(f"O  numero {numero} não é primo")
    