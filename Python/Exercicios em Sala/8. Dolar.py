#8 Faça um algoritmo que leia o salário de um funcionario e converta o salario dele para dolar (considere 5,25 o dolar)

salario = float(input("Digite o salario do funcionario: "))

conversao = salario / 5.25

print(f"O salario do funcionario em dolar é U$ {conversao:.2f}")