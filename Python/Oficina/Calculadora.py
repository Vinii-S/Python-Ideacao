
numero1 = float(input("Digite um numero: "))
escolha = input("Escolha uma operação:\n+ - * / \n")
numero2 = float(input("Digite outro numero: "))
if(escolha == "+"):
    resultadosoma= numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é {resultadosoma}")
elif(escolha == "-"):
    resultadosub = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é {resultadosub}")
elif(escolha == "*"):
    resultadomult = numero1 * numero2
    print(f"O resultado de {numero1} x {numero2} é {resultadomult}")
elif(escolha == "/"):
    resultadodiv = numero1 / numero2
    print(f"O resultado de {numero1} / {numero2} é {resultadodiv}")
    