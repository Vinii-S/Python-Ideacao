# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's' 'v' 'c' 'd';

cont = 0

while cont == 0:
    nome = input("Digite um nome maior que 3 caracteres: ")
    print(len(nome))
    if(len(nome)<3):
        print("Digite novamente")
        nome = input("Digite um nome maior que 3 caracteres: ")
    else:
        break
    idade = int(input("Digite uma idade entre 0 e 150: "))
    if(idade<0 and idade>150):
        print("Idade invalida, digite novamente.")