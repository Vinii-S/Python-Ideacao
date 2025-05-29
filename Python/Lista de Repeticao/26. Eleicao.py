qtdEleitores = int(input("Informe a quantiade de eleitores: "))
candidato1 = "Lula"
candidato2 = "Bolsonaro"
candidato3 = "Ciro"
cont1 = 0
cont2 = 0
cont3 = 0
for i in range(qtdEleitores):
    while True:
        print(f"\nEleitor {i+1}:")
        print(f"1 - {candidato1}\n2 - {candidato2}\n3 - {candidato3}")
        voto = int(input("Digite o número do candidato desejado: "))
        if(voto==1):
            cont1+=1
            print("Registrado Voto no candidato 1")
            break
        elif(voto==2):
            cont2+=1
            print("Registrado Voto no candidato 2")
            break
        elif(voto==3):
            print("Registrado Voto no candidato 3")
            cont3+=1
            break
        else:
            print("Numero incorreto, digite novamente")

print("\nResultado da Eleição:")
print(f"{candidato1}: {cont1} voto(s)")
print(f"{candidato2}: {cont2} voto(s)")
print(f"{candidato3}: {cont3} voto(s)")
        
if(cont1>cont2 and cont1>cont3):
    print(f"O ganhador foi o Candidato 1- {candidato1}")
elif(cont2>cont1 and cont2>cont3):
    print(f"O ganhador foi o Candidato 2- {candidato2}")
elif(cont3>cont1 and cont3>cont2):
    print(f"O ganhador foi o Candidato 3- {candidato3}")
elif(cont1==cont2 or cont1==cont3 or cont2==cont3):
    print("Empate na Eleição")