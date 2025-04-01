#5. Leia 3 números e imprima de forma decrescente
num1 = int(input("Digite o 1 valor: "))
num2 = int(input("Digite o 2 valor: "))
num3 = int(input("Digite o 3 valor: "))
aux = int
if(num1<num2):
    aux = num2
    num2 = num1
    num1 = aux
else:
    if(num3>num1):
        print(num3,num1,num2)
    else:
        if(num3>num2):
            print(num3,num2,num1)
        else: 
            print(num1,num2,num3)
"""
if(num1 >= num2) and (num2>=num3):
    print(num1,num2,num3)
elif(num1>=num3) and (num3>=num2):
    print(num1,num3,num2)
elif(num2>=num1) and (num1>=num3):
    print(num2,num1,num3)
elif(num2>=num3) and (num3>=num1):
    print(num2,num3,num1)
elif(num3>=num1) and (num1>=num2):
    print(num3,num1,num2)
else:
    print(num3,num2,num1)
  """   