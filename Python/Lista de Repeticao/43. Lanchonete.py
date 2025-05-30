print("Cardapio:\nEspecificação / Código / Preço")
print("Cachorro Quente / 100 / R$ 1,20\nBauru Simples / 101 / R$ 1,30\nBauru com ovo / 102 / R$ 1,50\nHambúrguer / 103 / R$ 1,20\nCheeseburguer / 104 / R$ 1,30\nRefrigerante / 105 / R$ 1,00")
total = 0
while True:
    codigo = input("Digite o código do produto ou sair para encerrar: ")
    if(codigo=="sair"):
        break
    quantidade = int(input("Digite a quantidade que deseja: "))
    if(int(codigo) == 100):
        total += (1.20 * quantidade)
    elif(int(codigo) == 101):
        total+= (1.30 * quantidade)
    elif(int(codigo) == 102):
        total += (1.50 * quantidade)
    elif(int(codigo) == 103):
        total += (1.20 * quantidade)
    elif(int(codigo) == 104):
        total += (1.30 * quantidade)
    elif(int(codigo) == 105):
        total += (1 * quantidade)
    
print(f"Seu pedido ficou com um total de R$ {total}")
