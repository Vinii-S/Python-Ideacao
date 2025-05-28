n = int(input("Digite o número de termos da sequencia de Fibonacci que você deseja: "))
a=0
b=1

if(n<=0):
    n=int(input("Digite um numero maior que 0: "))
elif n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c = a + b
        print(c)
        a = b
        b = c