import random

numero = random.randrange(1,10)
advinha = int(input("Adivinhe o número entre 0 e 10: "))
while numero!=advinha:
    advinha = int(input("Errou, digite outro numero entre 0 e 10: "))
    if(advinha==numero):
        print(f"Parabéns você acertou o número era {numero}.")  
        