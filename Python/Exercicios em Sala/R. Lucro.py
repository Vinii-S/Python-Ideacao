#18 Um comerciante comprou um produto e quer vende-lo com lucro de 45% se o valor da compra for menor que 20.00, caso contrario, o lucro sera de 30%.
#Leia o valor do produto e imprima o valor da renda de acordo com as taxas

valorProduto = float(input("Digite o valor que o produto foi comprado: "))

if(valorProduto<20):
    lucro = 1.45
    valorProduto*=lucro
    print(f"O produto precisa ser vendido por {valorProduto} para se ter um lucro de 45%")
else:
    lucro= 1.30
    valorProduto*=lucro
    print(f"O produto precisa ser vendido por {valorProduto} para se ter um lucro de 30%")