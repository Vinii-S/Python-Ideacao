popA = 80000
popB = 200000

crescimentoA = 1.03
crescimentoB= 1.015

anos = 0

print(f"A população do país A tem {popA} habitantes")
print(f"A população do país B tem {popB} habitantes")
while popA<=popB:
    popA = popA * crescimentoA
    popB = popB * crescimentoB
    anos+=1

print(f"Foram precisos {anos} anos para que a população do país A fosse {popA:.2f} e se tornasse maior ou igual ao país B com {popB:.2f} pessoas")