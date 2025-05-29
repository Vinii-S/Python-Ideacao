i= 1
total = 0
while True:
    produto = float(input(f"Produto {i}: R$ "))
    total += produto
    if produto == 0:
        print(f"Total: R$ {total}")
        pagamento = float(input("Dinheiro: R$ "))
        while pagamento<total:
                print("Dinheiro insuficiente")
                pagamento = float(input("Dinheiro: R$ "))
        troco = pagamento - total
        print(f"Troco: R$ {troco}")
        i=0
    if produto<0:
        break
    i+=1