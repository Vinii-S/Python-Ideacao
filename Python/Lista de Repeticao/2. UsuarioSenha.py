#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e
#voltando a pedir as informações.

cont = 0

while cont == 0:
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite uma senha: ")

    if(usuario!=senha):
        print("Conta criada com sucesso")
        break
    else:
        print("Nome de usuario nao pode ser igual a senha, digite de novo.")