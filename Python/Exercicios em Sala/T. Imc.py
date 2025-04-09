#20 Faca um algortimo que calcule o IMC de uma pessoa

peso = float(input("Informe seu pesso em Quilos (Kg): "))
altura = float(input("Informe sua altura em Metros (m): "))

imc= peso/altura**2

if(imc<=18.5):
    print(f"Seu IMC é {imc:.2f} e você é considerada uma pessoa magra")
elif(imc>=18.5 and imc<=24.9):
    print(f"Seu IMC é {imc:.2f} e você é considerada uma pessoa normal")
elif(imc>=25 and imc<=29.9):
    print(f"Seu IMC é {imc:.2f} e você é considerada uma pessoa com sobrepeso")
elif(imc>=30 and imc<=39.9):
    print(f"Seu IMC é {imc:.2f} e você é considerada uma pessoa obesa")
else:
    print(f"Seu IMC é {imc:.2f} e você é considerada uma pessoa com obesidade grave")