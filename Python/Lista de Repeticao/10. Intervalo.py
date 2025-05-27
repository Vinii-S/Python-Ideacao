num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if num1 < num2:
    for numero in range(num1 + 1, num2):  
        print(numero)
else:
    for numero in range(num2 + 1, num1):
        print(numero)