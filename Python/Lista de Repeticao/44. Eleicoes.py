candidato1 = "Lula"
candidato2 = "Bolsonaro"
candidato3 = "Ciro"
candidato4 = "Marina Silva"
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
while True:
        print(f"1 - {candidato1}\n2 - {candidato2}\n3 - {candidato3}\n4 - {candidato4}\n5 - Voto Nulo\n6 - Voto em Branco")
        voto = int(input("Digite o número do candidato desejado ou 0 para encerrar: "))
        if(voto==1):
            cont1+=1
            print("Registrado Voto no candidato 1")
            
        elif(voto==2):
            cont2+=1
            print("Registrado Voto no candidato 2")
            
        elif(voto==3):
            print("Registrado Voto no candidato 3")
            cont3+=1
            
        elif(voto==4):
            print("Registrado Voto no candidato 4")
            cont4+=1
        elif(voto==5):
            print("Registrado Voto Nulo")
            cont5+=1
        elif(voto==6):
            print("Registrado Voto nem Branco")
            cont6+=1
        elif(voto==0):
            break
        else:
            print("Numero incorreto, digite novamente")
            continue
porcentagemNulo = cont5 / (cont1+cont2+cont3+cont4+cont5+cont6) 
porcentagemBranco = cont6 / (cont1+cont2+cont3+cont4+cont5+cont6)
print("\nResultado da Eleição:")
print(f"{candidato1}: {cont1} voto(s)")
print(f"{candidato2}: {cont2} voto(s)")
print(f"{candidato3}: {cont3} voto(s)")
print(f"{candidato4}: {cont4} voto(s)")
print(f"Votos em Nulo: {cont5} voto(s)")
print(f"Votos em Branco: {cont6} voto(s)")
print(f"Porcentagem de votos nulos em relação ao total: {porcentagemNulo * 100}%")
print(f"Porcentagem de votos em Branco em relação ao total: {porcentagemBranco * 100}%")
