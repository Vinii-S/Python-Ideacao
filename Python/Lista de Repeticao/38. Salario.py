salario = 1000
aumento = 0.015
total = salario

for ano in range(1995,2026):
    if ano == 1995:
        print(f"Salario do ano {ano}: R$ {salario}")
        continue
    total *= (1 + aumento)
    if(ano>=1996):
        aumento = aumento * 2
    print(f"Salario do ano {ano}: R$ {total:.2f}")
        