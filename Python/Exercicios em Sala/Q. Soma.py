#17 Faca um algoritmo que leia 02 numeros e realize a soma. Se o valor somado for maior que 22, este devera ser apresentado somado-se a 8
#se o valor somado for menor ou igual a 22, este devera ser apresentado subtraindo-se 5

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2

if(soma>22):
    soma+=8
    print(f"A soma é maior que 22, entao e preciso acrescentar 8, resultado: {soma}")
else:
    soma-=5
    print(f"A soma é menor que 22, entao e preciso diminuir 5, resultado: {soma}")