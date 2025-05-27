popA = float(input("Informe a população do País A:"))
popB = float(input("Informe a população do País B:"))


crescimentoA = float(input("Informe a taxa de crescimento anual da população do País A em % : "))
crescimentoB = float(input("Informe a taxa de crescimento anual da população do País B em % : "))
crescimentoA = (crescimentoA / 100) + 1
crescimentoB = (crescimentoB / 100) + 1

anos = 0

print(f"A população do país A tem {popA} habitantes")
print(f"A população do país B tem {popB} habitantes")
if(popA>=popB):
    print("A população de A já é maior que a de B.")
else:
    while popA<=popB:
        popA = popA * crescimentoA
        popB = popB * crescimentoB
        anos+=1
    print(f"Foram precisos {anos} anos para que a população do país A fosse {popA:.2f} e se tornasse maior ou igual ao país B com {popB:.2f} pessoas")