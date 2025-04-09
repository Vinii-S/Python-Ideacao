#22 Dado tres lados de um triangulo, se a = b = c, o triangulo é equilatero. Se os dois valores sao iguais e um diferente é isoceles, se os 3 forem diferentes o triangulo é escaleno.

numA = int(input("Informe o valor do lado A: "))
numB = int(input("Informe o valor do lado B: "))
numC = int(input("Informe o valor do lado C: "))

if(numA==numB==numC):
    print("O triangulo é equilatero.")
elif (numA!=numB!=numC) and (numA!=numC):
    print("O triangulo é escaleno.")  
elif (numA != numB) and (numA==numC):
    print("O triangulo é isoceles.")
elif (numB != numC) and (numB==numA):
    print("O triangulo é isoceles.")
elif (numC != numA) and (numC==numB):
    print("O triangulo é isoceles.")