numero = int(input("Digite um número e descubra se ele é primo: "))
primo = True
divisiveis = []
for i in range(2,numero):
    if(numero%i==0):
        primo = False
        divisiveis.append(i)
        continue
    
if primo:
    print(f"O numero {numero} é primo")
else:
    print(f"O numero {numero} não é primo e é divisível pelos seguintes numeros: \n{divisiveis}")
    