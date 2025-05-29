codigosCidades = []
numerosVeiculos = []
numerosAcidentes = []
poucosAcidentes = []
for i in range(5):
    cidade = input("Digite o codigo da cidade: ")
    codigosCidades.append(cidade)
    veiculo = int(input("Digite o numero de veiculos da cidade: "))
    numerosVeiculos.append(veiculo)
    acidente = int(input("Digite o numero de acidentes da cidade: "))
    numerosAcidentes.append(acidente)
    if(veiculo<2000):
        poucosAcidentes.append(acidente)
        
maiorAcidentes = numerosAcidentes.index(max(numerosAcidentes))
menorAcidentes = numerosAcidentes.index(min(numerosAcidentes))
mediaVeiculos = sum(numerosVeiculos) / 5
mediaPoucos = sum(poucosAcidentes) / len(poucosAcidentes)

print(f"A cidade de número {codigosCidades[maiorAcidentes]} teve mais acidentes, sendo {numerosAcidentes[maiorAcidentes]}")
print(f"A cidade de número {codigosCidades[menorAcidentes]} teve menos acidentes, sendo {numerosAcidentes[menorAcidentes]}")
print(f"A media de veículos das 5 cidades é {mediaVeiculos:.2f}")
print(f"")