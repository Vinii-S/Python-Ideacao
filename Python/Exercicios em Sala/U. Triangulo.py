#21 Dado tres segmento de reta a,b e c, se:
#A+B>C; A+C>B; B+C>A estes podem formar um triangulo. De acordo com essa explicacao, escreva um algoritmo que ao ler 3 valores informe se podem formar um triangulo\
    
numA = int(input("Informe o valor de A: "))
numB = int(input("Informe o valor de B: "))
numC = int(input("Informe o valor de C: "))

if((numA+numB)>numC) and ((numA+numC)>numB) and ((numB+numC)>numA):
    print("É possível formar um triangulo com esses valores")
else:
    print("Não é possível formar um triangulo com esses valores")