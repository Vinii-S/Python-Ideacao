#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário
#informe um valor válido.

nota = 0

while nota>=0 and nota<=10:
 nota =  float(input("Digite uma nota entre 0 e 10: "))
    
 if(nota<0 or nota>10):
  print("Valor invalido, encerrando codigo.")
  break