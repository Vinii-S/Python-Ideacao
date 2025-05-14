# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's' 'v' 'c' 'd';

cont = 0

while cont == 0:
    nome = input("Digite um nome maior que 3 caracteres: ")
    if(len(nome)<3):
        print("Digite novamente")
        cont2 = 0
        while cont2==0:
            nome = input("digite um nome maior que 3 caracteres: ")
            if(len(nome)<3):
                cont2=0
            else:
                cont2=1
        
    idade = int(input("Digite uma idade entre 0 e 150: "))
    if(idade<0 or idade>150):
        print("Idade invalida, digite novamente.")
        cont3 = 0
        while cont3==0:
            idade = int(input("digite uma idade entre 0 e 150: "))
            if(idade<0 or idade>150):
                cont3=0
            else:
                cont3=1
    salario = float(input("Informe um salário maior que 0: "))
    if(salario<0):
        print("Salario informado incorreto, digite novamente.")
        cont4 = 0
        while cont4==0:
            salario = int(input("informe um salário maior que 0: "))
            if(salario<0):
                cont4=0
            else:
                cont4=1
    sexo = input("Informe seu sexo 'm' ou 'f': ")
    if(sexo.lower()!='m' and sexo.lower()!= 'f'):
        print("Sexo inválido, digite novamente.")
        cont5 = 0
        while cont5==0:
            sexo = input("informe seu sexo 'm' ou 'f': ")
            if(sexo.lower()!='m' and sexo.lower()!= 'f'):
                cont5=0
            else:
                cont5=1
    estado_civil = input("Informe seu estado civil, 's' 'v' 'c' 'd': ")
    if estado_civil.lower() not in ['s', 'v', 'c', 'd']:
        print("Estado civil invalido, digite novamente")
        cont6 = 0
        while cont6==0:
            estado_civil = input("Informe seu estado civil, 's' 'v' 'c' 'd': ")
            if estado_civil.lower not in ['s', 'c', 'v', 'd']:
                cont6=0
            else:
                cont6=1
    cont=1
print(f"Seu nome e {nome}.") # type: ignore
print(f"Voce tem {idade} anos.")
print(f"Seu salario e R$ {salario}")
print(f"Voce e do sexo {f}")
print(f"Seu estado civil e {estado_civil}")