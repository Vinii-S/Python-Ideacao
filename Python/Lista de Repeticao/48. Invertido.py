numero = int(input("Digite um número inteiro positivo: "))
caracteres = list(str(numero))
caracteres.reverse()

print(f"Numero digitado: {numero} , Numero invertido: {''.join(caracteres)}")