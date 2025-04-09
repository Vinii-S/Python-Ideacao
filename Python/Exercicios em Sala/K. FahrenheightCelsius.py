#11 Faça um programa que leia uma temperatura em graus Farehenint e transforme em Celsius

temp = float(input("Informe a temperatura em Fahrenheit: "))

celsius = ((temp -32) * 5) / 9

print(f"A temperatura de ºF {temp} é igual ºC {celsius:.2f} ")