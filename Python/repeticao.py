a = 0

while a==0:
    x = int(input("Digite o valor de X: "))
    if(x%2==0):
        print(f"o numero {x} e par")
    else:
        print(f"O numero {x} e impar")
    a = int(input("Se deseja parar, digite 1, se nao, digite 0: "))
    