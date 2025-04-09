#16 Faça um algoritmo que leia a idade de um atleta e informe se este atleta é Adulto, Juvenil, Infantil ou Mirim. Considere:
#Adulto >=18
#Juvenil >=14 e <18
#Infantil >=9 e <14
#Mirim <9

idade = int(input("Digite a idade do atleta: "))
if(idade>=18):
   print("O atleta é Adulto.")
elif(idade>=14) and (idade<18):
   print("O atleta é Juvenil.")
elif(idade>=9) and (idade<14):
   print("O atleta é Infantil.")
else:
    print("O atleta é Mirim.")
