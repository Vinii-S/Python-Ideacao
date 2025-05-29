numero = int(input("Informe de qual número você deseja saber a tabuada: "))
comeco = int(input("Começar por: "))
fim = int(input("Fim: "))

while fim<comeco:
        print("O começo não pode ser menor que o fim, digite novamente")
        comeco = int(input("Começar por: "))
        fim = int(input("Fim: "))
   
for i in range(comeco,fim+1):
    
    print(f"{numero} * {comeco} = {numero*comeco}")
    comeco +=1
    