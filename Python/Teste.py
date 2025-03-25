#Comentário é com #

a = int (input("Digite o valor de A: "))
b = int (input("Digite o valor de B: "))

Soma = a + b
Sub = a - b
Mult = a * b
Div = a / b
print(Soma)

#Imprimir a variavel envolvida com {} deixa usar no meio da string se vc colocar f antes
print(f"A soma de {a} + {b} é {Soma}")
print(f"A subtração de {a} - {b} é {Sub}")
print(f"A multiplicação de {a} * {b} é {Mult}")
print(f"A divisão de {a} / {b} é {Div}")

print(f"Valor de A {a}, Valor de B {b}")
aux = a
a = b
b = aux

print(f"Valor de A {a}, Valor de B {b}")
